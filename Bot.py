import os
import getpass
import logging
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Dict, Any
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException
from Constants import metadata_field_info as md_info
from Constants import template, db_path, embedding_model, llm_model, llm_temperature, logging_file_path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import markdown

app = FastAPI()
logging.basicConfig(filename=logging_file_path,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str


class AdminPayload(BaseModel):
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


def set_google_api_key():
    os.environ["GOOGLE_API_KEY"] = '<API-KEY-HERE>'


def initialize_embeddings_model():
    return GoogleGenerativeAIEmbeddings(model=embedding_model)


def initialize_llm():
    return ChatGoogleGenerativeAI(model=llm_model, temperature=llm_temperature, streaming=True,
                                  callbacks=[StreamingStdOutCallbackHandler()])


def initialize_chroma_db(embeddings_model):
    return Chroma(persist_directory=db_path,
                  embedding_function=embeddings_model, collection_metadata={"hnsw:space": "cosine", 'k': 4})


def initialize_retriever(llm, db):
    metadata_field_info = md_info
    document_content_description = "Brief summary"
    return SelfQueryRetriever.from_llm(
        llm,
        db,
        document_content_description,
        metadata_field_info,
        enable_limit=True,
        verbose=True,
        return_intermediate_steps=False,
    )


def initialize_chains(llm, retriever):
    combine_chain = create_stuff_documents_chain(llm, PromptTemplate.from_template(template))
    return create_retrieval_chain(retriever, combine_chain)


@app.on_event("startup")
def startup_event():
    set_google_api_key()
    embeddings_model = initialize_embeddings_model()
    llm = initialize_llm()
    db = initialize_chroma_db(embeddings_model)
    retriever = initialize_retriever(llm, db)
    global retrieval_chain, chroma_db
    retrieval_chain = initialize_chains(llm, retriever)
    chroma_db = db


@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    question = request.question.lower().replace('è', 'e').replace('é', 'e')
    try:
        response = retrieval_chain.invoke({'input': question})
        answer = response['answer']
        context_used = response['context']
        logger.info(f'Question: {question}---- answer: {answer}---- context: {context_used}')
        return QueryResponse(answer = markdown.markdown(response['answer']))
    except OutputParserException as e:
        logger.error(f'Question: {question}----OutputParserException: {e}')
        raise HTTPException(status_code=500, detail="filter couldn't be processed by lark")
    except Exception as e:
        logger.error(f'Question: {question}----Error: {e}')
        raise HTTPException(status_code=500, detail='error occurred while trying to respond')


@app.post("/admin/add-document")
async def add_document(request: AdminPayload):
    logger.info(f"Received new document content: {request.content} with metadata: {request.metadata}")
    try:
        document = Document(
            page_content=request.content,
            metadata=request.metadata
        )
        chroma_db.add_documents(documents=[document])
        logger.info("Document successfully added to the vector database.")
        return {"message": "Document successfully added tdocko the vector database."}
    except Exception as e:
        logger.error(f'Error while trying to add document: {e}')
        raise HTTPException(status_code=500, detail=f'Error while trying to add document: {e}')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_index():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0" , port = 8000)

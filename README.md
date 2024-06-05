# FSTT-Chatbot

## Introduction

This project focuses on developing a chatbot fine-tuned on custom context based on French language models (LLMs), specifically for a case study at FSTT. The objective is to establish a smart chatbot using Retrieval Augmented Generation (RAG), LangChain, and Vector Databases, fine-tuned with a small French corpus from FSTT and related courses. By integrating these advanced NLP techniques and tools, the chatbot aims to provide accurate and contextually relevant responses, enhancing user interaction and information retrieval in the educational domain.

## Project Structure

```
├── Bot.py
├── Constants.py
├── README.md
├── requirements.txt
├── static
│   └── (static files)
├── fsttchatbot
│   ├── __init__.py
│   ├── views.py
│   └── (other files)
└── __pycache__
    └── (cache files)
```

## Modelisation and Conception

### Front End

1. *User Question*: The user submits a question via an HTTP POST request.

### Back End

1. *Retrieval Chain*:
    - *Self Query*: The query is combined with a predefined prompt template and attribute information.
    - *LLM*: The language model receives the prompt formed from the template and the user’s query.

2. *Chroma DB*:
    - *Similarity Search*: Chroma DB performs a similarity search based on metadata filters and the query.
    - *Combined Docs Chain*: The contextual documents found are combined to form a chain of documents.

3. *Large Language Model (LLM)*:
    - *Prompt*: The combined contextual documents are passed to the language model.

## Frameworks and Tools

### Python

Used for various parts of the project, including scripting and backend development.

### BeautifulSoup

Utilized for web scraping tasks to gather additional data.

### Flask

Framework used for building the backend of the application.

### Transformers

Library used for implementing and fine-tuning the Language Model.

## Application Details

### Choice of FastAPI or Flask for the Backend

The decision-making process involved evaluating the needs for asynchronous capabilities and performance, leading to the selection of Flask for this project due to its simplicity and extensive documentation.

### DevOps Integration for Continuous Integration and Deployment

The project integrates DevOps practices to ensure continuous integration and deployment, enhancing the development workflow and maintaining code quality.

## Single Page Application (SPA)

### Reasons for Choosing SPA Architecture

SPA architecture was chosen to provide a seamless and dynamic user experience, reducing the need for full-page reloads and improving interaction speed.

### Benefits and Challenges of SPA

*Benefits*:
- Improved user experience
- Faster interactions

*Challenges*:
- Increased complexity in client-side logic
- Potential SEO issues

## Implementation

The implementation involved setting up the project structure, integrating necessary frameworks and tools, and developing the core functionalities of the chatbot, including the retrieval and response generation processes.

## Application

The application aims to assist users by providing accurate and contextually relevant responses to their questions, leveraging advanced NLP techniques and tools to enhance the educational experience.

<div align="center">

<img src="https://github.com/AymanAitAhmed/FSTT-Chatbot/blob/main/screenshots/interface_light_theme.jpg" width="40%">

<img src="https://github.com/AymanAitAhmed/FSTT-Chatbot/blob/main/screenshots/interface_dark_theme.jpg" width="40%">

</div>
<div align="center">

<img src="https://github.com/AymanAitAhmed/FSTT-Chatbot/blob/main/screenshots/conversation.jpg" width="40%">

<img src="https://github.com/AymanAitAhmed/FSTT-Chatbot/blob/main/screenshots/admin.jpg" width="40%">

</div>

## Conclusion

The FST Chatbot project demonstrates the potential of integrating modern NLP techniques and tools to create intelligent and contextually aware chatbots. This project serves as a valuable case study in the educational domain, showcasing the capabilities of fine-tuned language models in providing meaningful user interactions.

const chatInput = document.querySelector("#chat-input");
const sendButton = document.querySelector("#send-btn");
const chatContainer = document.querySelector(".chat-container");
const themeButton = document.querySelector("#theme-btn");
const deleteButton = document.querySelector("#delete-btn");
const addDocButton = document.querySelector("#add-doc-btn");
const formContainer = document.querySelector(".form-container");
const documentContentInput = document.querySelector("#document-content");
const metadataContainer = document.querySelector("#metadata-container");
const addMetadataButton = document.querySelector("#add-metadata-btn");
const submitDocumentButton = document.querySelector("#submit-document-btn");
const cancelDocumentButton = document.querySelector("#cancel-document-btn");

let userText = null;
const API_URL = "/ask";
const ADD_DOC_URL = "/admin/add-document";

const loadDataFromLocalstorage = () => {
    const themeColor = localStorage.getItem("themeColor");

    document.body.classList.toggle("light-mode", themeColor === "light_mode");
    themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";

    const defaultText = `<div class="default-text">
        <h1>Chatbot FST Tanger</h1>
        <p>Commencez une conversation et posez vos questions sur la FST Tanger.<br> Votre historique de chat sera affiché ici.</p></div>`

    chatContainer.innerHTML = localStorage.getItem("all-chats") || defaultText;
    chatContainer.scrollTo(0, chatContainer.scrollHeight); 
}

const createChatElement = (content, className) => {
    const chatDiv = document.createElement("div");
    chatDiv.classList.add("chat", className);
    chatDiv.innerHTML = content;
    return chatDiv;
}

const deleteChats = () => {
    if (confirm("Are you sure you want to delete all the chats?")) {
        localStorage.removeItem("all-chats");
        loadDataFromLocalstorage();
    }
}

deleteButton.addEventListener("click", deleteChats);

const handleOutgoingChat = () => {
    userText = chatInput.value.trim();
    if (!userText) return;

    chatInput.value = "";
    chatInput.style.height = `${initialInputHeight}px`;

    const html = `<div class="chat-content">
                    <div class="chat-details">
                        <img src="/static/img/user.png" alt="user-img">
                        <p>${userText}</p>
                    </div>
                </div>`;

    const outgoingChatDiv = createChatElement(html, "outgoing");
    chatContainer.querySelector(".default-text")?.remove();
    chatContainer.appendChild(outgoingChatDiv);
    chatContainer.scrollTo(0, chatContainer.scrollHeight);

    const typingHtml = `<div class="chat-content">
                            <div class="chat-details">
                                <img src="/static/img/bot.png" alt="chatbot-img">
                                <div class="typing-animation">
                                    <div class="typing-dot" style="--delay: 0.2s"></div>
                                    <div class="typing-dot" style="--delay: 0.3s"></div>
                                    <div class="typing-dot" style="--delay: 0.4s"></div>
                                </div>
                            </div>
                        </div>`;
    const typingDiv = createChatElement(typingHtml, "incoming");
    chatContainer.appendChild(typingDiv);
    chatContainer.scrollTo(0, chatContainer.scrollHeight);

    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            question: userText
        })
    })
    .then(response => response.json())
    .then(data => {
        const answerHtml = `<div class="chat-content">
                                <div class="chat-details">
                                    <img src="/static/img/bot.png" alt="chatbot-img">
                                    <div style="
                                    /* gap: 10px; */
                                    /* margin-bottom: 10px; */
                                    display: flex;
                                    flex-direction: column;
                                    gap: 10px;">                                    <p>${data.answer}</p></div>
                                </div>
                            </div>`;
        const incomingChatDiv = createChatElement(answerHtml, "incoming");
        chatContainer.appendChild(incomingChatDiv);
        chatContainer.scrollTo(0, chatContainer.scrollHeight);

        typingDiv.remove();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

sendButton.addEventListener("click", handleOutgoingChat);

themeButton.addEventListener("click", () => {
    document.body.classList.toggle("light-mode");
    localStorage.setItem("themeColor", themeButton.innerText);
    themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";
});

const initialInputHeight = chatInput.scrollHeight;
chatInput.addEventListener("input", () => {
    chatInput.style.height =  `${initialInputHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleOutgoingChat();
    }
});

const handleAddDocument = () => {
    formContainer.style.display = "flex"; // Show the form
}

const handleCancelDocument = () => {
    formContainer.style.display = "none"; 
}

const handleAddMetadata = () => {
    const metadataContainerDiv = document.createElement("div");
    metadataContainerDiv.classList.add("metadata-row");

    const metadataKeyInput = document.createElement("input");
    const metadataItemInput = document.createElement("input");

    metadataKeyInput.type = "text";
    metadataItemInput.type = "text";

    metadataKeyInput.className = "metadata-key-input";
    metadataItemInput.className = "metadata-item-input";

    metadataKeyInput.placeholder = "Enter metadata key";
    metadataItemInput.placeholder = "Enter metadata item";

    metadataContainerDiv.appendChild(metadataKeyInput);
    metadataContainerDiv.appendChild(metadataItemInput);

    metadataContainer.appendChild(metadataContainerDiv);
}

const handleSubmitDocument = () => {
    const content = documentContentInput.value.trim();
    const metadataKeyInputs = document.querySelectorAll(".metadata-key-input");
    const metadataItemInputs = document.querySelectorAll(".metadata-item-input");

    const metadata = {};

    metadataKeyInputs.forEach((keyInput, index) => {
        const key = keyInput.value.trim();
        const item = metadataItemInputs[index].value.trim();

        if (key && item) {
            metadata[key] = item;
        }
    });

    if (!content || Object.keys(metadata).length === 0) {
        alert("Please enter content and at least one metadata pair.");
        return;
    }

    const documentData = {
        content: content,
        metadata: metadata
    };

    fetch(ADD_DOC_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(documentData)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        handleCancelDocument();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error while adding document: ' + error);
    });
}

addDocButton.addEventListener("click", handleAddDocument);
cancelDocumentButton.addEventListener("click", handleCancelDocument);
addMetadataButton.addEventListener("click", handleAddMetadata);
submitDocumentButton.addEventListener("click", handleSubmitDocument);

loadDataFromLocalstorage();

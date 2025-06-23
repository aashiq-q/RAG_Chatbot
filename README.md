# 📚 Hybrid RAG + LLM ChatBot with Streamlit

**A powerful conversational assistant that combines Large Language Model (LLM) capabilities with Retrieval-Augmented Generation (RAG) for context-aware, document-grounded responses — all within an interactive Streamlit web app.**

![Chatbot Screenshot](https://github.com/aashiq-q/RAG_Chatbot/blob/main/Rag_chatbot.png)
---

## 🚀 **Overview**

This project lets you interact with an AI assistant that works in **two modes**:

* ✅ **LLM Mode:** If no PDF is uploaded, it answers using only the base language model and remembers the conversation.
* 📑 **RAG Mode:** If you upload a PDF, it uses the document as a knowledge base. The model retrieves relevant chunks and answers based on your content.

It’s a **hybrid chatbot** — blending general language understanding with precise, context-specific answers from your own documents.

---

## 🗂️ **Tech Stack**

| Tool                        | Purpose                                            |
| --------------------------- | -------------------------------------------------- |
| **Streamlit**               | User-friendly web interface                        |
| **LangChain**               | Manages RAG pipelines & chaining                   |
| **FAISS**                   | Efficient local vector store for similarity search |
| **Hugging Face Embeddings** | Converts document chunks into vectors              |
| **ChatGroq LLM**            | Fast and capable language model backend            |
| **Unstructured PDF Loader** | Extracts text from uploaded PDFs                   |

---

## ✨ **Features**

* ✅ **Conversational memory** — remembers your previous questions in the session.
* 📄 **Upload PDF** — chatbot retrieves accurate answers from your custom document.
* 🔁 **Automatic fallback** — removes document knowledge when you delete the file, reverting to pure LLM mode.
* ⚡ **Fast semantic search** — uses FAISS for quick document retrieval.
* 🖥️ **Simple to run** — deploys easily via Streamlit.

---

## 📥 **How It Works**

1. **Upload your PDF**
   The app processes it, splits it into overlapping text chunks, and converts them into embeddings.

2. **Ask any question**
   The system retrieves the most relevant chunks and feeds them along with your question to the LLM.

3. **Get precise answers**
   If no PDF is uploaded, it defaults to normal LLM chat mode with memory.

4. **Delete the file**
   The vector store is cleared and the bot uses only the LLM.

---

## ⚡ **Setup Instructions**

### 1️⃣ **Clone the repo**

```bash
git clone https://github.com/aashiq-q/RAG_Chatbot.git
cd RAG_chatbot
```

### 2️⃣ **Create a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Set up your environment**

Create a `.env` file in the root folder:
You can use any llm api key you want example openai

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
```

or export it in your shell:

```bash
export GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
```

---

### 5️⃣ **Run the app**

```bash
streamlit run chatbot.py
```

Open the link shown in your terminal to interact with your chatbot.

---

## 🗂️ **Project Structure**

```
├── chatbot.py         # Main Streamlit app
├── requirements.txt  # Python dependencies
├── .env              # Your API key (not committed to Git)
└── README.md         # Project description
```

---

## 🔑 **Environment Variables**

| Variable       | Description                             |
| -------------- | --------------------------------------- |
| `GROQ_API_KEY` | Your API key for accessing the Groq LLM |

---

## ✅ **To Do**

* [ ] Support for multiple documents
* [ ] Better error handling for large files
* [ ] Deploy to Streamlit Cloud
* [ ] Dockerize the project
* [ ] Add unit tests

---

## 🤝 **Contributing**

Pull requests are welcome! If you find a bug or have a feature idea, feel free to open an issue or fork the repo.

---

## 📜 **License**

This project is licensed under the **MIT License** — feel free to use and adapt it for your own projects.

---

## 🌟 **Acknowledgements**

* [LangChain](https://github.com/langchain-ai/langchain)
* [Streamlit](https://streamlit.io/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Hugging Face](https://huggingface.co/)
* [Groq](https://groq.com/)

---

## 📬 **Contact**

📫 Reach me **[aashiqconnects@gmail.com](aashiqconnectsgmail.com)**

Feel free to reach out if you have any questions or ideas to improve this project!

**Happy Building! 🚀✨**

---

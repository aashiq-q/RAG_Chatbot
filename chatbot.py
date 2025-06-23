import os
import tempfile
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=groq_api_key, model_name="llama-3.1-8b-instant")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
    st.session_state.conversationchain = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )

    st.session_state.qachain = None
    st.session_state.vectorstore = None

st.title("ChatBot with RAG!")

uploaded_file = st.file_uploader("Upload a PDF file(Optional)", type="pdf")

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = UnstructuredPDFLoader(tmp_file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    st.session_state.vectorstore = vectorstore
    retriever = vectorstore.as_retriever()
    st.session_state.qachain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever = retriever,
    )

    st.success("File Processed Successfully!")

if st.session_state.vectorstore:
    if st.button("Clear Uploaded File"):
        st.session_state.vectorstore = None
        st.session_state.qachain = None
        st.success("File Cleared Successfully!")

query = st.text_input("Ask me anything", label_visibility="collapsed")

if query:
    if st.session_state.qachain:
        answer = st.session_state.qachain.run(query)
        st.write("Answer (RAG):", answer)

    else:
        response =st.session_state.conversationchain.run(query)
        st.write("Answer (LLM):", response)



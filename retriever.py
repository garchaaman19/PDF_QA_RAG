from config import GROQ_API_KEY
from langchain_groq import ChatGroq
import os
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

def initialize_rag_model(vectorstore):
    """
    Initialize rag model using Groq llm and retrieve the documents
    return retrieval chain
    """
    retriever = vectorstore.as_retriever()
    llm = ChatGroq(model="llama3-8b-8192",temperature=0.5)
    chain = load_qa_chain(llm, chain_type="stuff")  # 'stuff' is a default method for handling multiple documents
    qa_retrieval_chain = RetrievalQA(combine_documents_chain=chain, retriever=retriever, return_source_documents=True)
    return qa_retrieval_chain

def chatbot_interface(query, qa_retrieval_chain):
    result = qa_retrieval_chain({'query': query})['result']
    return result
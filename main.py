import streamlit as st  
import os
from utils import get_file_hash
from store_data_and_create_embeddings import clear_chroma_db,create_embeddings
from retriever import initialize_rag_model,chatbot_interface
from extract_data_from_pdf import extract_tables_and_text

if __name__=='__main__':

    st.title("PDF Q&A Chatbot")

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        pdf_path = os.path.join("./uploads", uploaded_file.name)
        os.makedirs("./uploads", exist_ok=True) 
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        file_hash = get_file_hash(pdf_path)
        
        if "file_hash" not in st.session_state or st.session_state.file_hash != file_hash:
            st.write("Processing uploaded PDF...")
            st.session_state.file_hash = file_hash
            st.session_state.pdf_path = pdf_path 
            clear_chroma_db()

            text_data, table_data = extract_tables_and_text(pdf_path)
            vectorstore = create_embeddings(text_data, table_data)
            
            qa_retrieval_chain = initialize_rag_model(vectorstore)
            st.session_state.qa_retrieval_chain = qa_retrieval_chain
            vectorstore = None
            st.write("The PDF has been processed, You can now ask questions")
        else:
            st.write("The PDF already exists, You can now ask questionss")
        user_query = st.text_input("Ask a question about the PDF:")
        
        if user_query and "qa_retrieval_chain" in st.session_state:
            response = chatbot_interface(user_query, st.session_state.qa_retrieval_chain)
            st.write("Response:", response)

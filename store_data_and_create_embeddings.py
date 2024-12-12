
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma


def create_embeddings(text_data, table_data):
    """
    Create embeddings and store in Chroma db
    """
    combined_data = text_data + table_data  
    embeddings = SentenceTransformerEmbeddings()
    vectorstore = Chroma.from_texts(combined_data, embeddings, persist_directory="./chroma_db")  
    return vectorstore

def clear_chroma_db():
    """
    Clear the chroma_db storage to avoid using previous embeddings
    """
    vectorstore = Chroma(persist_directory="./chroma_db")
    all_ids = vectorstore.get()['ids']
    if all_ids:
        vectorstore.delete(ids=all_ids)

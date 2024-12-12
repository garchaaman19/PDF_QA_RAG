# PDF Q&A Chatbot

This bot allows users to upload a PDF file and ask questions about its content. It will extracts text and table data from the PDF, creates embeddings, and uses a **Retrieval-Augmented Generation (RAG)** model to answer user queries. The interface is powered by **Streamlit**.

---

## **Features**
- **Upload PDF Files**: Upload PDF files directly through a web-based interface.
- **Text and Table Extraction**: Extracts both plain text and table content from PDFs.
- **Embeddings and Vector Store**: Embeds the PDF data using **SentenceTransformerEmbeddings** and stores it in **ChromaDB**.
- **Query Answering**: Can ask questions, and the system responds with relevant information extracted from the PDF.

---

## **Project Structure**
```
├── main.py  # Main script to run the Streamlit app
├── requirements.txt  # Python dependencies
├── chroma_db/  # Directory to store ChromaDB embeddings
├── uploads/  # Directory to store uploaded PDFs
├── demo_screenshots/  # Screenshots of app demo
```

---

## **Installation**

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/garchaaman19/PDF_QA_RAG.git>
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```


## **Usage**

1. **Run the Application**
   ```bash
   streamlit run main.py
   ```

2. **Upload a PDF**
   - Click on the "Upload a PDF" button to select and upload a PDF file.

3. **Q&A**
   - Once the PDF is processed, enter your question in the input box.

---

## **Possible Enhancements**
- **Add Support for Multiple PDFs**: Allow users to query multiple PDFs simultaneously.

---

## **Dependencies**

- **Streamlit**: For the interactive user interface.
- **PyMuPDF (fitz)**: For extracting text from PDFs.
- **Hugging Face Transformers**: For table extraction using **TableTransformerForObjectDetection**.
- **ChromaDB**: For embedding storage and retrieval.
- **LangChain**: To enable the Q&A chain.

All required dependencies are listed in **requirements.txt**. please install them before using:
```bash
pip install -r requirements.txt
```

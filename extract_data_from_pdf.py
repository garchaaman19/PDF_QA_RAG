from langchain.document_loaders import PyPDFLoader
from transformers import TableTransformerForObjectDetection, DetrImageProcessor
import fitz  
from PIL import Image 



def read_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents


def extract_tables_and_text(pdf_path):
    """
    Extract tables and text from the given PDF using TableTransformer and DetrImageProcessor
    return text data, table data
    """
    table_data = []
    text_data = []
    model = TableTransformerForObjectDetection.from_pretrained("microsoft/table-transformer-detection")
    processor = DetrImageProcessor.from_pretrained("microsoft/table-transformer-detection")
    #NOTE alternate method AutoImageProcessor for processing, but DETR works better with table transformer as it is made for object detection.
    
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text_content = page.get_text("text")
        text_data.append(text_content)
        pix = page.get_pixmap() 
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        
        for i, label in enumerate(outputs.logits.argmax(-1).tolist()):
            if label == 1:  
                table_data.append(outputs.pred_boxes[i].tolist())
    
    pdf_document.close()
    
    return text_data, table_data

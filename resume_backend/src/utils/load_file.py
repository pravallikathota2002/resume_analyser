from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from markitdown import MarkItDown
from langchain_core.documents import Document
from PIL import Image
from pytesseract import pytesseract
from ..rag.embeddings import EmbeddingPipeline
from ..rag.vector_store import FaissVectorStore


# here we are checking the resume files docx or images and loading the content

def load_resume_files(file_path):
    print("============= inside the loading resume files using markitdown============")
    # need to check the type of the folder or image 
    file_type = str(file_path).split(".")[1]
    try:
        if file_type not in {"pdf", "docx", "xlsx"}:
            return "File type is not supported, only pdf or docx or xlsx is supported"
        if file_type in {"pdf","docx","xlsx"}:
            md = MarkItDown()
            result = md.convert(file_path)
            print(result)
            text = result.text_content
            docs = [
                Document(page_content=text)
            ]
        
            # after loading the data we can create embeddings and save in vector store here only for rag purpose
            # every resume what ever the user uploading, while uploading only we are creating embeddings and saving in vector store
            store = FaissVectorStore("faiss_store")
            store.build_from_documents(docs)
            return result.text_content
        else:
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)
            return text.strip()

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    


# from langchain_community.document_loaders import PyPDFLoader

# def load_pdf(file_path):
#     # loader = PyMuPDF4LLMLoader(file_path)
#     # docs = loader.load()
#     # # need to add the time taking to extrac the resume 
#     # print(docs[0])
#     # return docs
#     loader = PyPDFLoader(file_path)
#     return loader.load()
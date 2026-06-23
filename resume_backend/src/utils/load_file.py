from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from markitdown import MarkItDown
from PIL import Image
from pytesseract import pytesseract


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
from fastapi import FastAPI,File, UploadFile
from src.utils.save_files import save_resume_files
from src.utils.load_file import load_resume_files
from src.parsers.parseresumetojson import ParseResume

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/uploadfile")
def resume_uploader(file:UploadFile):
    # 1. get the file 
    print("================= insdie the resume uploader router ====================")
    print("===================== file name ==============", file.filename)

    # 2. save the file in local or storage directory 

    #  it will return the path of the resume
    saved_path = save_resume_files(file)

    # 3. loading the data , it will extract the content
    resume_text = load_resume_files(saved_path)
    
    # 4. need to check the what i need to extract from the content
    parser = ParseResume(resume_text)
    res = parser.get_JSON()

    return res
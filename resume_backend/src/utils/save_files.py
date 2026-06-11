import os
import shutil

base_path = os.path.dirname(os.path.abspath(__file__))
directory_path = os.path.dirname(base_path)

def save_resume_files(file):
    print("=============== inside the saving resume files =================")

    resumes_dir = os.path.join(directory_path, "data", "resumes")

    # Create folder if it doesn't exist
    os.makedirs(resumes_dir, exist_ok=True)

    file_path = os.path.join(resumes_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
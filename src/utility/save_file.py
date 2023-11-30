from .generate_file_name import generate_file_name
from src.constants import FILES_FOLDER
import os
from fastapi import UploadFile


def save_file(file: UploadFile):
    filename = generate_file_name()
    path = os.path.join(FILES_FOLDER, filename)
    with open(path, "wb") as f:
        f.write(file.file.read())

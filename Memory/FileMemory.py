import random
import json
import string
import pymupdf as fitz


class FileMemory:
    def __init__(self, file, pdf_path):
        self.file = file

    def save_file(result, difficulty):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=5))
        filename = f"{difficulty}_recipe_{random_string}"
        with open(f"./Recipes/{filename}.txt", 'w') as a:
            a.write("recipe" + result)

    def extract_text_from_pdf(pdf_path):
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
        return text

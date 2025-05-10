import random
import json
import string


class FileMemory:
    def __init__(self, file):
        self.file = file
#"./Memory/"+
    def save_file(result, difficulty):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=5))
        filename = f"{difficulty}_recipe_{random_string}"
        with open(f"./Recipes/{filename}.txt", 'w') as a:
            a.write("recipe" + result)

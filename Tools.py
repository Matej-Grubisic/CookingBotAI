import json
from langchain.tools import Tool
import requests

def recognize_language(inputs_str:str)->str:
    inputs = json.loads(inputs_str)
    code = inputs["code"]
    obj = {"codesnippet": code, "language": "string"}
    response = requests.post('http://ai.easv.dk:8989/tools/langrecog/?temp=0', json=obj)
    return response.json()

recognizeTool = Tool(
    name="RecognizeLanguage",
    func=lambda inputs: recognize_language(inputs),
    description="Recognizes the language of a given code snippet."
)


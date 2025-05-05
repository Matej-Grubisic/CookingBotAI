import json
from langchain.tools import Tool
import requests

def easy_tool(inputs_str:str)->str:
    inputs = json.loads(inputs_str)
    message = inputs["message"]
    food_style = inputs["food_style"]
    obj = {"message": message, "food_style": {food_style}}
    response = requests.post('http://localhost:8000/recipes/easy', json=obj)
    return response.json()

easyTool = Tool(
    name="easyRecipeTool",
    func=lambda inputs: easy_tool(inputs),
    description="Gives an easy recipe to the user."
)




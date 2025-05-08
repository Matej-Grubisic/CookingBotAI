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

# Medium Recipe Tool
def medium_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    message = inputs["message"]
    food_style = inputs["food_style"]
    obj = {"message": message, "food_style": food_style}
    response = requests.post('http://localhost:8000/recipes/medium', json=obj)
    return response.json()

# Hard Recipe Tool
def hard_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    message = inputs["message"]
    food_style = inputs["food_style"]
    obj = {"message": message, "food_style": food_style}
    response = requests.post('http://localhost:8000/recipes/hard', json=obj)
    return response.json()

# Pro Recipe Tool
def pro_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    message = inputs["message"]
    food_style = inputs["food_style"]
    obj = {"message": message, "food_style": food_style}
    response = requests.post('http://localhost:8000/recipes/pro', json=obj)
    return response.json()

easyTool = Tool(
    name="easyRecipeTool",
    func=lambda inputs: easy_tool(inputs),
    description="Gives an easy recipe to the user."
)

mediumTool = Tool(
    name="mediumRecipeTool",
    func=lambda inputs: medium_tool(inputs),
    description="Gives a medium-level recipe to the user."
)

hardTool = Tool(
    name="hardRecipeTool",
    func=lambda inputs: hard_tool(inputs),
    description="Gives a hard-level recipe to the user."
)

proTool = Tool(
    name="proRecipeTool",
    func=lambda inputs: pro_tool(inputs),
    description="Gives a professional-level recipe to the user."
)



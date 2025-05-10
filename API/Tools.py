import json
from langchain.tools import Tool
import requests

def easy_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    obj = {
        "message": inputs["message"],
        "food_style": inputs["food_style"]
    }
    try:
        response = requests.post('http://localhost:8000/recipes/easy', json=obj)
        response_data = response.json()
        recipe = response_data.get("Easy", None)
        return recipe if recipe else {"error": "Recipe not found"}
    except Exception as e:
        return {"error": f"Failed to parse response: {str(e)}"}

def medium_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    obj = {
        "message": inputs["message"],
        "food_style": inputs["food_style"]
    }
    try:
        response = requests.post('http://localhost:8000/recipes/medium', json=obj)
        response_data = response.json()
        recipe = response_data.get("Medium", None)
        return recipe if recipe else {"error": "Recipe not found"}
    except Exception as e:
        return {"error": f"Failed to parse response: {str(e)}"}

def hard_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    obj = {
        "message": inputs["message"],
        "food_style": inputs["food_style"]
    }
    try:
        response = requests.post('http://localhost:8000/recipes/hard', json=obj)
        response_data = response.json()
        recipe = response_data.get("Hard", None)
        return recipe if recipe else {"error": "Recipe not found"}
    except Exception as e:
        return {"error": f"Failed to parse response: {str(e)}"}

def pro_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    obj = {
        "message": inputs["message"],
        "food_style": inputs["food_style"]
    }
    try:
        response = requests.post('http://localhost:8000/recipes/pro', json=obj)
        response_data = response.json()
        recipe = response_data.get("Pro", None)
        return recipe if recipe else {"error": "Recipe not found"}
    except Exception as e:
        return {"error": f"Failed to parse response: {str(e)}"}

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


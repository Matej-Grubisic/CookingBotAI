
import uvicorn
from fastapi import FastAPI
from langchain.chains import ConversationChain
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_community.chat_models import ChatOllama
from API.Chains import easy_chain, medium_chain, hard_chain, pro_chain
from pydantic import BaseModel
from Agent import run_agent


app = FastAPI()


class AgentRequest(BaseModel):
    message: str
    food_style: str
    difficulty: str

class UserRequest(BaseModel):

    message: str
    food_style: str
    difficulty: str



llm = ChatOllama(model="ChatAI")



@app.post("/recipes/easy")
async def easy_recipe(request: UserRequest):

    generated_answer = easy_chain.invoke({
        "message": request.message,
        "food_style": request.food_style,
    })
    return {"Easy Recipe: " : generated_answer}

@app.post("/recipes/medium")
async def medium_recipe(request: UserRequest):

    generated_answer = medium_chain.invoke({
        "message": request.message,
        "food_style": request.food_style,

    })
    return { "Medium Recipe: " : generated_answer}

@app.post("/recipes/hard")
async def hard_recipe(request: UserRequest):
    generated_answer = hard_chain.invoke({
        "message": request.message,
        "food_style": request.food_style,

    })
    return {"Hard Recipe: ": generated_answer}

@app.post("/recipes/pro")
async def pro_recipe(request: UserRequest):
    generated_answer = pro_chain.invoke({
        "message": request.message,
        "food_style": request.food_style,
    })

    return {"Pro Recipe: ": generated_answer}

def format_user_input(level: str, message: str, food_style: str) -> str:
    return f"Give me a {level} recipe for this: {message}. The food style is {food_style}."

@app.post("/recipes/{level}")
async def generate_recipe(level: str, request: UserRequest):
    formatted_input = format_user_input(level, request.message, request.food_style)
    result = run_agent(level, formatted_input)
    return {f"{level.capitalize()} Recipe": result}

@app.post("/agent-recipe")
async def agent_recipe(request: AgentRequest):
    formatted = f"Give me a {request.difficulty} recipe for this: {request.message}. The food style is {request.food_style}."
    result = run_agent(request.difficulty, formatted)
    return {"response": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
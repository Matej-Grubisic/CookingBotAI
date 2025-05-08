
import uvicorn
from fastapi import FastAPI
from langchain.chains import ConversationChain
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_community.chat_models import ChatOllama
from API.Chains import easy_chain, medium_chain, hard_chain, pro_chain
from pydantic import BaseModel


app = FastAPI()



class UserRequest(BaseModel):
    message: str
    food_style: str

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
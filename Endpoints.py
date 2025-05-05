from fastapi import FastAPI
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    request: str
    food_style: str
    difficulty: str

@app.get("/recipes/easy")
async def EasyRecipe(request: str, food_style: str):
    model = Ollama(model="deepseek-r1:1.5b")

    prompt = PromptTemplate.from_template(
        "Generate a {food_style} recipe that is easy for a beginner to make for this request:\n\n{request}"
    )

    chain = prompt | model

    generated_answer = chain.invoke({
        "request": request,
        "food_style": food_style,
    })
    return generated_answer

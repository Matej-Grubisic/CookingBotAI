import json

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.tools import Tool
import requests
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_ollama import OllamaEmbeddings, ChatOllama
from Memory.FileMemory import FileMemory as fe


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

def pdf_tool(inputs_str: str) -> str:
    inputs = json.loads(inputs_str)
    llm = ChatOllama(model="llama3.2")

    pdf_text = fe.extract_text_from_pdf(inputs["file_path"])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents([Document(page_content=pdf_text)])

    embedding_model = OllamaEmbeddings(model="nomic-embed-text")

    vector_store = FAISS.from_documents(documents, embedding_model)

    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_store.as_retriever())

    query = "Give me the best, most popular, and most convenient recipes from the provided PDF text, Give me the page list if possible. Make sure its cohesive. Keep responses natural, as if having a real conversation with a professional cook."
    response = qa_chain.run(query)

    return f"PDF: {response}"

pdfTool = Tool(
    name="pdfCookbookTool",
    func=lambda inputs: pdf_tool(inputs),
    description="Gives a general overview of the best recipes of the PDF cookbook provided"
)

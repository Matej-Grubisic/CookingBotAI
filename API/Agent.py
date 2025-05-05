from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from pymongo import MongoClient
from langchain_ollama import ChatOllama
from Memory.MongoMemory import MongoMemory
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from Tools import easyTool



#MONGO NOT BEING USED CURRENTLY
client = MongoClient("mongodb://localhost:27017/")
db = client["chat_memory"]
collections = db["conversations"]

llm = ChatOllama(model="ChatAI")

template = """You are a World class chef.
Here is our conversation history on the subject of cooking:
History:{history}
User: {input}
"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

mongo_memory = MongoMemory(collections)

print(mongo_memory)

memory = ConversationBufferMemory(memory_key="history", input_key="input")


previous_messages = mongo_memory.load_messages()



for msg in previous_messages:
    parts = msg.split("\n")
    memory.chat_memory.add_user_message(parts[0].replace("User: ", ""))
    memory.chat_memory.add_ai_message(parts[1].replace("Bot: ", ""))

chat_history = mongo_memory.load_messages()
#^^^ NOT BEING USED CURRENTLY


def run_agent(difficulty: str, input_data: str):
    agent = initialize_agent(
        tools=[easyTool],
        llm = llm,
        #memory=memory,
        verbose=True,
        prompt=prompt,
    )



    #llm = chooseModel()
    #agent.llm = llm

    tool_map = {
        "easy": easyTool,
        #"medium": mediumTool,
        #"hard": hardTool,
        #"professional": proTool,
    }

    tool = tool_map.get()
    if tool:
        return tool.invoke(input_data)
    else:
        return agent.invoke(input_data)

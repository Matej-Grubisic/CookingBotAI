from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
# from langchain.memory import ConversationBufferMemory  # Commented out because you're not using memory
from API.Tools import easyTool, mediumTool, hardTool, proTool
from langchain_core.prompts import PromptTemplate
from pymongo import MongoClient
from Memory.MongoMemory import MongoMemory


client = MongoClient("mongodb://localhost:27017/")
db = client["chat_memory"]
collections = db["conversations"]
mongo_memory = MongoMemory(collections)


llm = ChatOllama(model="llama3.2")


template = """You are a World class chef.
Here is our conversation history on the subject of cooking:
History:{history}
User: {input}
"""
prompt = PromptTemplate(input_variables=["history", "input"], template=template)


# memory = ConversationBufferMemory(memory_key="history", input_key="input")  # Commented out since memory is not being used

# previous_messages = mongo_memory.load_messages()  # Commented out since memory is not being used
# for msg in previous_messages:  # Commented out since memory is not being used
#     parts = msg.split("\n")  # Commented out since memory is not being used
#     memory.chat_memory.add_user_message(parts[0].replace("User: ", ""))  # Commented out since memory is not being used
#     memory.chat_memory.add_ai_message(parts[1].replace("Bot: ", ""))  # Commented out since memory is not being used

def run_agent(difficulty: str, input_data: str):
    agent = initialize_agent(
        tools=[easyTool, mediumTool, hardTool, proTool],
        llm=llm,
        verbose=True,
    )

    tool_map = {
        "easy": easyTool,
        "medium": mediumTool,
        "hard": hardTool,
        "pro": proTool
    }

    tool = tool_map.get(difficulty.lower())

    if tool:
        try:
            result = tool.invoke(input_data)
            if isinstance(result, dict):
                return result.get(f"{difficulty.capitalize()} Recipe: ", "❌ Recipe not found")
            return result
        except Exception as ex:
            return f"❌ Error invoking tool: {str(ex)}"
    else:
        try:
            return agent.run(input_data)
        except Exception as ex:
            return f"❌ Error running agent: {str(ex)}"
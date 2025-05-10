from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
# from langchain.memory import ConversationBufferMemory  # Commented out because you're not using memory
from API.Tools import easyTool, mediumTool, hardTool, proTool
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from Memory.FileMemory import FileMemory as fe

llm = ChatOllama(model="llama3.2")



template = """
You are an AI chatbot designed to give the best and most optimized recipes for cooking you have. The user will provide the food style category and the difficulty of the recipe as a parameter, and you must initiate and give him the best recipe that fits that category.
Your responses should be: Engaging and relevant to the subject. Inquisitive, asking follow-up questions to maintain a natural flow. Informative, drawing on broad and deep knowledge about cooking. Adaptive in accordance to the user's ingredients. If the user changes their mind about a recipe, food style category or difficulty, smoothly transition and give a new answer. Avoid straying from anything that wasn't before mentioned by the user. Keep responses natural, as if having a real conversation with a professional cook."
Here are recipes you've already gave: {history},

"""
prompt = PromptTemplate(input_variables=["history", "input"], template=template)


memory = ConversationBufferMemory(memory_key="history", input_key="input")

previous_messages = ()

#for msg in previous_messages:
#     parts = msg.split("\n")
#     memory.chat_memory.add_user_message(parts[0].replace("User: ", ""))
#     memory.chat_memory.add_ai_message(parts[1].replace("Bot: ", ""))

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
            fe.save_file(result, difficulty)
            if isinstance(result, dict):
                return result.get(f"{difficulty.capitalize()} Recipe: ", "❌ Recipe not found")
            return result
        except Exception as ex:
            return f"❌ Error invoking tool: {str(ex)}"
    else:
        return agent.invoke(input_data)

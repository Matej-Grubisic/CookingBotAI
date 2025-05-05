from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
#from src.Tools import explainTool,generateTool,translateTool,styleTool,codeQualityTool,recognizeTool

def chooseModel(request_type: str):
    model = Ollama(model="deepseek-r1:1.5b")
    return model

def run_agent(task_type: str, input_data: str):
    agent = initialize_agent(
        #tools=[translateTool, styleTool, codeQualityTool, recognizeTool],
        llm=chooseModel(task_type),
        verbose=True
    )
    #llm = chooseModel()
    #agent.llm = llm

    tool_map = {
        #"easy": explainTool,
        #"medium": generateTool,
        #"hard": translateTool,
        #"professional": styleTool,
    }

    tool = tool_map.get(task_type)
    if tool:
        return tool.invoke(input_data)
    else:
        return agent.invoke(input_data)
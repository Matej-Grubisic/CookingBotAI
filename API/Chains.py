from langchain_community.llms import Ollama  # for completion-style models
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

llm = Ollama(model="llama3.2")

easy_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional chef specialized in giving out easy recipes."),
    ("human", "Give me a recipe of {food_style} category that a chef who knows nothing can make based on my request:\n\n{message}")
])

easy_chain = RunnableSequence(
    easy_prompt | llm | StrOutputParser()
)

medium_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a World class chef specialized in giving out recipes that a amateur cook can make."),
    ("human", "Give me a recipe of {food_style} category that an amateur chef can make based on my request:\n\n{message}")
])

medium_chain = RunnableSequence(
    medium_prompt | llm | StrOutputParser()
)

hard_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a World class chef specialized in giving out hard to make recipes."),
    ("human", "Give me a recipe of {food_style} category that only a professional chef can make based on my request:\n\n{message}")
])

hard_chain = RunnableSequence(
    hard_prompt | llm | StrOutputParser()
)

pro_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a World class level chef specialized in giving out extremely difficult recipes."),
    ("human", "Give me a recipe of {food_style} category that only a professional chef can make based on my request:\n\n{message}")
])

pro_chain = RunnableSequence(
    pro_prompt | llm | StrOutputParser()
)


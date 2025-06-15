from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()

template1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "write a 5 line summary on {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

print(chain.invoke("Cricket"))
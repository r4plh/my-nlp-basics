from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4o")

response = llm.invoke("WHen was NBA started")

print(response)
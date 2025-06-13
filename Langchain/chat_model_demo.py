from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")

response = model.invoke("When is Cricket WC started in India?")

print(response)
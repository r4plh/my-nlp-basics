from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_histroy = [
    SystemMessage(content="You're a helpful chatbot")
]

while True:
    user_input = input("You:")
    chat_histroy.append(HumanMessage(content = user_input))
    if user_input == "exit":
        break
    response = model.invoke(chat_histroy)
    chat_histroy.append(AIMessage(content= response.content))
    print(f"AI : {response.content}")

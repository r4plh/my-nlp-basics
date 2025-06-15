from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_histroy = []


template = ChatPromptTemplate([
        ('system','You are a helpful chatbot'),
        ('human','Explain what is {topic} in 2 lines')]
)


user_input = str(input("Enter the topic"))
initial_msg = template.invoke({'topic':user_input})

print(initial_msg)

chat_histroy.append(initial_msg)

while True:
    result = model.invoke(chat_histroy)
    chat_histroy.append(AIMessage(content=result.content))
    print("AI: ",result.content)          
    user_input = input("You:")
    if user_input == "exit":
        break
    chat_histroy.append(HumanMessage(content=user_input))
  
# Logic is correct altough code deosn't work
# Took dyanmic prompt varible from user and made chain of chainPromptTemplate | model -> then did chain.ivoke()
# now in bot strat from AI message and start saving the chat history and then finally upload it in a db somwhere
# Then again ewhen user contiue then load it via Message place holden from DB and continue the same AI/human chatbot 
# Then update the chat history in the DB and so on



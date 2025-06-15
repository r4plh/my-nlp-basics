from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

chat_prompt_template = (
    [
        ('system','You are a helpful chatbot'),
        MessagesPlaceholder(variable_name=chat_history)
        ('human','{query}')
    ]
)

user_input = input("You:")

chat_prompt_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})
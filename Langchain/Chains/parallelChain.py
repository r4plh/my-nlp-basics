from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

model1 = ChatOpenAI(model="gpt-3.5-turbo")
model2 = ChatOpenAI(model="gpt-4o")

parser = StrOutputParser()

load_dotenv()

prompt1 = PromptTemplate(
    template =  "Give 5 points about the personal life , biography type of this player - {player}",
    input_variables=['player']
)

prompt2 = PromptTemplate(
    template = "Generate 5 points about the particular sports the {player} has played his majority of life.",
    input_variables=['player']
)

prompt3 = PromptTemplate(
    template = "Now you have to blend the points and make another 5 moints which have come from biography {life} and sports from {sport}",
    input_variables=['life','sport']
)

parallel_chain = RunnableParallel({
    'life': prompt1 | model1 | parser,
    'sport': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

print(chain.invoke({"player" : 'AB de Villiers'}))



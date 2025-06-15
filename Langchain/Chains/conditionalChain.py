from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal,List

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Recog(BaseModel):

    sentiment : Literal['positive','negative'] = Field(description="This is telling the sentiment involved")

parser1 = PydanticOutputParser(pydantic_object=Recog)

prompt1 = PromptTemplate(
    template= "Classify whether the feedback text has positive or negative sentiment -> feedback is {feedback} \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser1.get_format_instructions()}
)

classiy_chain = prompt1 | model | parser1

result0 = classiy_chain.invoke({'feedback':"This is a terrible bat , it have no english cover and wood is also not proper"})
print(type(result0))
print(result0.sentiment)

prompt2 = PromptTemplate(
    template="Give response to this positive feedback -> {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Give response to this negative feedback -> {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser), # calling x.sentiment as we're calling from pydantic object
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
     RunnableLambda(lambda x: "could not find sentiment")
)

chain = classiy_chain | branch_chain

text = "This is a terrible bat , it have no english cover and wood is also not proper"

print(chain.invoke({'feedback':text}))
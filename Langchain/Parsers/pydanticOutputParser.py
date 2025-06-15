from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

model = ChatOpenAI(model= "gpt-3.5-turbo")

class Unique(BaseModel):

    name: str = Field(description="Name of the person"),
    age: int = Field(gt=18, description = "AGe of the person")
    city: str = Field(description='Name of the city')


parser = PydanticOutputParser(pydantic_object=Unique)

template1 = PromptTemplate(
    template="Generate the required about the country {country} \n {format_instructions}"  ,
    input_variables=['country'],
    partial_variables={'format_instructions': parser.get_format_instructions()}

)

chain = template1 | model | parser

print(chain.invoke({'country':"India"}))
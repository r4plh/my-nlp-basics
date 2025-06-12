from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional , Annotated

class Patient(BaseModel):

    name : Annotated[str,Field(max_length=50,description="name of the patient that is coming at the clinic for health check up",title="Name of the pateint",examples=["Aman",'r4plh'])] # For data validation
    age : int = Field(gt=0,lt=100) # For data validation
    email : EmailStr
    weight : Annotated[float, Field(gt=0,strict=True)] # For data validation , strictness on coerce
    contact_details : Optional[Dict[str,str]] = None

def name_and_age(patient:Patient):

    print(patient.name)
    print(patient.age)

patient_info = {"name":"Aman","email":"qwe@gmail.com","age":'43',"contact_details":{'email':'abc@gmail.com','phone':'124455'}}

patient1 = Patient(**patient_info)

name_and_age(patient1)
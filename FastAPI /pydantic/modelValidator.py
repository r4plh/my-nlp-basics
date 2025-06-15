from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Dict, Optional , Annotated

class Patient(BaseModel):

    name : Annotated[str,Field(max_length=50,description="name of the patient that is coming at the clinic for health check up",title="Name of the pateint",examples=["Aman",'r4plh'])] # For data validation
    age : int = Field(gt=0,lt=100) # For data validation
    email : EmailStr
    weight : Annotated[float, Field(gt=0,strict=True)] # For data validation , strictness on coerce
    contact_details : Optional[Dict[str,str]] = None

    @model_validator(mode='after')
    def check(cls,model): # Here we pass the entire model coz we wanna validate two fields and combination of them so used model validator
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("emergency contact should be present")
        return model




def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)
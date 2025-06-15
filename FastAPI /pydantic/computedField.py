from pydantic import BaseModel, EmailStr, Field, field_validator, computed_field
from typing import List, Dict, Optional , Annotated

class Patient(BaseModel):

    name : Annotated[str,Field(max_length=50,description="name of the patient that is coming at the clinic for health check up",title="Name of the pateint",examples=["Aman",'r4plh'])] # For data validation
    age : int = Field(gt=0,lt=100) # For data validation
    height : float = Field(description="height of the person")
    email : EmailStr
    weight : Annotated[float, Field(gt=0,strict=True)] # For data validation , strictness on coerce
    contact_details : Optional[Dict[str,str]] = None

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('BMI', patient.bmi)
    print('updated')


patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)

from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):

    name : str
    age : int
    email : EmailStr
    contact_details : Optional[Dict[str,str]] = None

def name_and_age(patient:Patient):

    print(patient.name)
    print(patient.age)

patient_info = {"name":"Aman","email":"qwe@gmail.com","age":'43',"contact_details":{'email':'abc@gmail.com','phone':'124455'}}

patient1 = Patient(**patient_info)

name_and_age(patient1)
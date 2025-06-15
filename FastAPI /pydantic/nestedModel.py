from pydantic import BaseModel , Field

# This is useful when you want to save a complex field so you define a pydantic class seprately for that class , like here for address
class Address(BaseModel):

    city : str
    area : str
    pin : int

class Person(BaseModel):

    name : str = Field(description="name of person")
    age : int = Field(description="age of person")
    address : Address


address1 = {'city':'mumbai','aread':'bandra','pin':1343211}

address_py = Address(**address1)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Person(**patient_dict)

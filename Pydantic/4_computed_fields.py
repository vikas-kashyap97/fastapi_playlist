from pydantic import BaseModel, EmailStr,AnyUrl, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedIn_url)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data Updated")

patient_info = {'name':'Vikas', 'email':'vikas@icici.com', 'linkedIn_url': 'https://www.linkedin.com/in/vikas-kashyap97/', 'age': '25', 'weight': 55, 'height': 1.72, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'911'}}

patient1 = Patient(**patient_info) 

update_patient_data(patient1)

# This code defines a Patient model using Pydantic and calculates the patient's BMI automatically using a computed field. The update_patient_data function prints all patient details, including the computed BMI.
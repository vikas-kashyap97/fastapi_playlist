from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(
        max_length=50,
        title='Name of the patient',
        description='Please provide the name of the patient',
        examples=['Vikas', 'Vikas Kashyap', 'V. K. Kashyap']
    )]
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int = Field(gt=0, lt=100)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[Optional[bool], Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_items=5)]
    contact_details: Dict[str, str]

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedIn_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data Updated')

patient_info = {
    'name': 'Vikas',
    'email': 'vikas@gmail.com',
    'linkedIn_url': 'https://www.linkedin.com/in/vikas-kashyap97/',
    'age': 25,
    'weight': 58,
    'contact_details': {'phone': '8542000000'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)

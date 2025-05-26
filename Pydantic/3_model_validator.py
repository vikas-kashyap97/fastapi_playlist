from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient should be older than 60 must have a contact number')
        return model
    

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedIn_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data Updated")

patient_info = {
    'name': 'Vikas',
    'email': 'vikas@sbi.com',
    'linkedIn_url': 'https://www.linkedin.com/in/vikas-kashyap97/',
    'age': 65,
    'weight': 58.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '8542000000', 'emergency': '911'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)

# This code uses Pydantic to validate patient data. It includes a model-level check to ensure that patients over 60 have an emergency contact. The update_patient_data function prints the validated details.
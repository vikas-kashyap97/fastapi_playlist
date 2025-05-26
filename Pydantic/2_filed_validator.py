from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['hdfc.com', 'sbi.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if value < 18:
            raise ValueError('Patient must be at least 18 years old')
        return value

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
    'age': 25,
    'weight': 58.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '8542000000', 'emergency': '911'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)


# This code defines a Patient model using Pydantic to validate and clean patient data. It ensures the name is in uppercase, email is from specific domains, and age is at least 18. The update_patient_data function prints the validated patient details.

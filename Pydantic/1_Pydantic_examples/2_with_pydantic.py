from pydantic import BaseModel, ValidationError

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('Data Inserted')
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('Data Updated')
    
patient_info= {'name': 'Vikas', 'age': 25}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

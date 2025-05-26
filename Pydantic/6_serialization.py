from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'Hardoi', 'state': 'Uttar Pradesh', 'pin': '241001'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Vikas', 'gender': 'Male', 'age': 25, 'address': address1}
patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)
temp2 = patient1.model_dump_json(exclude_unset=True)

print(temp)
print(temp2)
print(type(temp))
print(type(temp2))


# This code defines a Patient model with nested Address using Pydantic.
# It creates an instance with basic patient info, converts it to a Python dictionary (model_dump) and JSON string (model_dump_json), and prints their types.

# temp → dictionary (Python dict)
# temp2 → JSON string (str)
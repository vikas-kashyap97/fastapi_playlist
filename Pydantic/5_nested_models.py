from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Hardoi', 'state': 'Uttar Pradesh', 'pin': '241001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'vikas', 'gender': 'male', 'age': 25, 'address': address1}

patient1 = Patient(**patient_dict)
print(patient1)



# This code defines two Pydantic models: Address and Patient, where Patient includes a nested Address model. It creates and prints a patient instance with structured address data.


# What are Nested Models?

# Nested models in Pydantic are models used as fields inside other models. In this example:
# Address is a model with fields: city, state, and pin.
# Patient includes an address field, which is of type Address.
# This allows for cleaner, reusable, and more organized data structures, especially when dealing with complex or hierarchical data like user profiles, locations, or configurations.


# Better organization of related data (e.g., vitals, address, insurance)
# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)
# Readability: Easier for developers and API consumers to understand
# Validation: Nested models are validated automatically—no extra work needed
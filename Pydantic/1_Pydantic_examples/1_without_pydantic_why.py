def insert_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:
        if age < 0:
            raise TypeError("Age can not be a negative number")
        else:
            print(name)
            print(age)
            print('Data Inserted')
    else:
        raise TypeError('Incorrect data type')
    
insert_patient_data('Vikas', 20)

def update_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:
       print(name)
       print(age)
       print('Data Updated')
    else:
        raise TypeError('Incorrect data type')
    
update_patient_data('Vikas', 20)


#  Summary
# Instead of manually checking each input's type and constraints in every function, we use Pydantic to ensure data integrity in a clean, consistent, and scalable way. This leads to more reliable code, better developer experience, and fewer bugs in production.



# ✅ Why Use Pydantic Instead
# Pydantic offers:

# ✅ Automatic runtime validation of types and constraints
# ✅ Clear and structured error messages
# ✅ Cleaner, reusable models
# ✅ Declarative syntax (focus on what the data should look like, not how to check it)
# ✅ Better integration with modern tools (e.g., FastAPI, validation layers)
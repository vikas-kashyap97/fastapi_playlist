# 🚀 FastAPI + Pydantic Examples

This repository demonstrates the **core concepts of FastAPI and Pydantic**, ranging from basic validation to complex model structures, computed fields, and real-world CRUD operations using JSON as a mock database.

> GitHub Repository: [fastapi_playlist](https://github.com/vikas-kashyap97/fastapi_playlist.git)

---

## 📁 Project Structure

```
FASTAPI/
│
├── __pycache__/                    # Python cache files
├── Pydantic/
│   └── 1_Pydantic_examples/        # Core Pydantic concept examples
│       ├── 1_without_pydantic_why.py
│       ├── 2_with_pydantic.py
│       ├── 3_bit_complex_pydantic.py
│       ├── 2_filed_validator.py
│       ├── 3_model_validator.py
│       ├── 4_computed_fields.py
│       ├── 5_nested_models.py
│       └── 6_serialization.py
│
├── venv/                           # Python virtual environment
├── .gitignore                      # Files to ignore by git
├── main.py                         # Main FastAPI application
├── patients.json                   # JSON file to simulate data storage
└── Capture.PNG                     # Screenshot showing project structure
```

---

## 🧰 Tech Stack

- **FastAPI**: Web framework for building APIs quickly.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **JSON**: Used as a mock database.
- **Uvicorn**: ASGI server for serving FastAPI apps.

---

## ▶️ Running the App

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
uvicorn main:app --reload
```

Open Swagger UI at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📦 Features Demonstrated

### ✅ Basic Routes

- `GET /` – Welcome message.
- `GET /about` – API description.

### 📋 View Data

- `GET /view` – View all patient records.
- `GET /patient/{patient_id}` – Fetch a specific patient's data.

### 🔄 Sort Data

- `GET /sort` – Sort patients by `height`, `weight`, or computed `bmi`.

Query Parameters:
- `sort_by`: `"height" | "weight" | "bmi"` (required)
- `order`: `"asc" | "desc"` (default: `asc`)

### ➕ Add Data

- `POST /create` – Add a new patient record.

Sample Payload:

```json
{
  "id": "P001",
  "name": "John Doe",
  "city": "New York",
  "age": 35,
  "gender": "male",
  "height": 1.75,
  "weight": 70,
  "blood_group": "A+-",
  "blood_pressure": "120/80",
  "medical_conditions": "None",
  "medications": "None"
}
```

> Computed Fields:
> - `bmi`: Auto-calculated BMI.
> - `verdict`: Auto-generated health status based on BMI.

### ✏️ Update Data

- `PUT /edit/{patient_id}` – Update any existing patient fields.

### ❌ Delete Data

- `DELETE /delete/{patient_id}` – Remove a patient record.

---

## 🧠 Pydantic Concepts Covered

Located in `Pydantic/1_Pydantic_examples/`:

| File                            | Concept Covered                            |
|---------------------------------|---------------------------------------------|
| 1_without_pydantic_why.py       | Manual validation & its limitations         |
| 2_with_pydantic.py              | Basic model definition with Pydantic        |
| 3_bit_complex_pydantic.py       | Slightly advanced model structures          |
| 2_filed_validator.py            | Field-level validation with `@validator`    |
| 3_model_validator.py            | Entire model validation                     |
| 4_computed_fields.py            | Use of `@computed_field` in Pydantic        |
| 5_nested_models.py              | Nested models and compositions              |
| 6_serialization.py              | Serialization and model export techniques   |

---

## 📂 Data File

All records are stored in `patients.json`. This simulates a lightweight local database, suitable for learning and prototyping.

---

## 🧪 Testing

Test the endpoints with:
- Swagger UI
- Postman
- Curl or httpie

---

## 📸 Screenshot

This project includes a screenshot (`Capture.PNG`) for easy navigation and reference to the file structure in VS Code.

---

## 🙌 Credits

This project is authored to help learners understand **how FastAPI and Pydantic work together** to build clean, scalable APIs with modern Python.

> GitHub: [https://github.com/vikas-kashyap97/fastapi_playlist.git](https://github.com/vikas-kashyap97/fastapi_playlist.git)

---



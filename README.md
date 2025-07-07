# Python Flask Backend for Elevated SDLC 2025

## 📌 Purpose

This project serves as an educational backend template for teaching **REST API fundamentals** and **introducing Python Flask** to beginner developers and undergraduates. It emphasizes clean architecture, in-memory data storage, and practical CRUD operations for hands-on learning.


## 🚀 Features

1. **Simple RESTful API** built using Flask
2. **In-memory TODO management** (no external database needed)
3. Supports:
   - Creating, reading, updating, and deleting TODO items
   - Optional filtering by title (`search`) and completion status (`done`)
4. Modular codebase with:
   - Blueprint routing
   - Basic model abstraction
5. Clean JSON responses
6. Beginner-friendly virtual environment setup


## 🗂️ Project Structure

```plaintext
flask_app/
├── app/
│   ├── __init__.py            # Flask app factory
│   ├── extensions.py          # Placeholder for future extensions
│   ├── models/
│   │   └── todo.py            # Todo model class
│   └── routes/
│       ├── __init__.py        # Blueprint registration
│       └── todo_routes.py     # API endpoints for TODOs
├── run.py                     # App entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── venv/                      # (Excluded) Virtual environment
```

## 📘 API Endpoints

Base URL: `http://localhost:5000/api/v1/todos`

### GET `/`
Returns a list of all TODO items.

#### Optional Query Parameters:
- `search` (string): Filter by partial match on title  
  e.g., `?search=milk`
- `done` (boolean): Filter by completion status (`true` or `false`)  
  e.g., `?done=true`

#### Response:
```json
[
  {
    "id": 1,
    "title": "Buy milk",
    "description": "Get 2 liters of milk",
    "due_date": "2025-06-25",
    "created_date": "2025-06-23T10:00:00",
    "done": true
  }
]
```

### 🔹 POST `/`

Creates a new TODO item.

#### 🔸 Request Body (JSON)
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, and bread",
  "due_date": "2025-06-30"
}
```

### 🔹 PUT `/<id>`

Updates an existing TODO item by its ID.

#### 🔸 Path Parameter
- `id` (integer): The ID of the TODO to update

#### 🔸 Request Body (JSON)
```json
{
  "title": "Finish report",
  "description": "Add summary section",
  "due_date": "2025-07-01",
  "done": true
}
```

### 🔹 DELETE `/<id>`

Deletes a TODO item by its ID.

#### 🔸 Path Parameter
- `id` (integer): The ID of the TODO to delete

#### ✅ Success Response (204 No Content)
```json
{
  "message": "Deleted"
}
```

## ⚙️ Prerequisites

- [Python 3.10](https://www.python.org/downloads/release/python-3109/)
- A text editor (eg: VS Code) or an IDE (eg: Jetbrains PyCharm)
- A stable internet connection

## 📋 Instructions

1. Clone or download this repository.
2. Open your command-line tool of choice.
3. Confirm that you are using Python 3.10 by running ```python --version```.
4. Create a new virtual environment by running ```python -m venv venv``` in the root project directory.
5. Activate the created virtual environment by running one of the below commands based on your command-line tool of choice.
    - ```source venv/Scripts/activate``` (Git Bash on Windows)
    - ```venv\Scripts\activate``` (CMD on Windows)
    - ```.\venv\Scripts\Activate.ps1``` (Powershell on Windows)
    - ```source venv/bin/activate``` (Linux/MacOS).
6. Install the project dependencies by running ```pip install -r requirements.txt```.
7. Start the backend by running ```python run.py```.
8. Navigate to ```localhost:5000/api/v1``` on your browser of choice.

## 💡 License

This project is open for educational use and modification. Feel free to fork and expand as needed for learning purposes.
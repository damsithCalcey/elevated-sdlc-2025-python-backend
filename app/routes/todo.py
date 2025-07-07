from flask import Blueprint, request, jsonify, abort
from datetime import datetime

todo_bp = Blueprint('todo', __name__, url_prefix='/api/v1/todos')
todos= []

def get_todo_by_id(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        abort(404, description="TODO not found")
    return todos[todo_id]


@todo_bp.route('', methods=['GET'])
def get_todos():
    return jsonify(todos)


@todo_bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = get_todo_by_id(todo_id)

    return jsonify(todo)


@todo_bp.route('', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos),
        "title": data.get("title"),
        "description": data.get("description", ""),
        "due_date": data.get("due_date"),
        "created_date": datetime.now().isoformat(),
        "done": data.get("done", False)
    }
    todos.append(new_todo)

    return jsonify(new_todo), 201


@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = get_todo_by_id(todo_id)

    todo["title"] = data.get("title", todo["title"])
    todo["description"] = data.get("description", todo["description"])
    todo["due_date"] = data.get("due_date", todo["due_date"])

    if "done" in data:
        done_value = data.get("done")
        todo["done"] = str(done_value).lower() == "true"

    return jsonify(todo), 200


@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos

    todo = get_todo_by_id(todo_id)
    todos.remove(todo)
    
    return jsonify({"message": "Deleted"}), 204

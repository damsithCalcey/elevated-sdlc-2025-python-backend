from flask import Blueprint, request, jsonify
from typing import List

from app.models.todo import Todo

todo_bp = Blueprint('todo', __name__, url_prefix='/api/v1/todos')
todos: List[Todo] = []

@todo_bp.route('', methods=['GET'])
def get_todos():
    search_filter = request.args.get('search', '').lower()
    done_filter = request.args.get("done")

    if done_filter is not None:
        done_filter = str(done_filter).lower() == "true"

    filtered = [
        todo.to_dict()
        for todo in todos
        if (search_filter in todo.title.lower() if search_filter else True)
        and (todo.done == done_filter if done_filter is not None else True)
    ]

    return jsonify(filtered)


@todo_bp.route('', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = Todo(
        title=data.get("title"),
        description=data.get("description", ""),
        due_date=data.get("due_date")
    )
    
    todos.append(new_todo)

    return jsonify(new_todo.to_dict()), 201


@todo_bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo.id == todo_id:
            todo.update(data)
            
            return jsonify(todo.to_dict())

    return jsonify({"error": "TODO not found"}), 404


@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t.id != todo_id]

    return jsonify({"message": "Deleted"}), 204

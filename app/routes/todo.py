from flask import Blueprint, request, jsonify

todo_bp = Blueprint('todo', __name__, url_prefix='/api/v1')
todos = []

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@todo_bp.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todos) + 1,
        "task": data.get("task"),
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201


@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo_item in todos:
        if todo_item["id"] == todo_id:
            todo_item["task"] = data.get("task", todo_item["task"])
            todo_item["done"] = data.get("done", todo_item["done"])
            return jsonify(todo_item)
    return jsonify({"error": "Todo not found"}), 404


@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Deleted"}), 204

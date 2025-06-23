from .main import main_bp
from .todo import todo_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(todo_bp)

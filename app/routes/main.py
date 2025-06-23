from flask import Blueprint

main_bp = Blueprint('main', __name__, url_prefix='/api/v1')

@main_bp.route('/')
def index():
    return "Welcome to the Flask TODO API"
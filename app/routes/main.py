from flask import Blueprint

main_bp = Blueprint('main', __name__, url_prefix='/api/v1')

@main_bp.route('/', methods=['GET'])
def index():
    return "Welcome to the Flask TODO API"
from flask import Flask
from .extensions import cors
from .routes import register_blueprints

def create_app():
    app = Flask(__name__)
    cors.init_app(app)

    register_blueprints(app)
    
    return app

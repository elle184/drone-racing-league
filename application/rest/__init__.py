import os
from flask import Flask
from flask_jwt_extended import JWTManager
from .modelos import User

def create_app(config_name) :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:postgres@localhost:5432/idrl"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', 'secret_phrase')

    jwt = JWTManager(app)

    return app


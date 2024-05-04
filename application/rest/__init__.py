from flask import Flask

def create_app(config_name) :
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:postgres@localhost:5432/idrl"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    return app


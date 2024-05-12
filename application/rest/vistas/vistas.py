from ..modelos import db, User, usuario_schema
from flask_restful import Resource
from flask import request, abort
from flask_jwt_extended import create_access_token

class VistaEjemplo(Resource) :

    def get(self):
        return "Hello, World!"

class VistaCrearUsuario(Resource):
    def post(self):
        try :
            if None != request.json :
                user = User(
                    password = request.json['password']
                    , user = request.json['username']
                    , email = request.json['email']
                )

                db.session.add(user)
                db.session.commit()
                return usuario_schema.dump(user), 201
        except Exception :
            abort(406, "Person already exists")

class VistaLogin(Resource):
    def post(self):
        user = User.query.filter(
            User.user == request.json['username']
            , User.password == request.json['password']).first()

        if user is not None:
            access_token = create_access_token(identity = user.id)
            return {"message" : "Inicio de sesión exitoso", "token" : access_token}
        else:
            abort(404, f"Person with last name {request.json['username']} not found")
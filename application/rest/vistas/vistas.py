from ..modelos import db, User, usuario_schema
from flask_restful import Resource
from flask import request, abort

class VistaEjemplo(Resource) :

    def get(self):
        return "Hello, World!"

class VistaCrearUsuario(Resource):
    def post(self):
        try :
            print(request.json)

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
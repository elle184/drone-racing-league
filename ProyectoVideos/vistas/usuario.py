# usuario.py

# Remove: from datetime import datetime
from flask import make_response, abort
from flask_restful import Resource
from modelo import db
from modelo import Usuario, usuario_schema, usuario_schema
class VistaLogin(Resource):
    def get(lname,email):
        usuario = Usuario.query.filter(Usuario.lname == lname).one_or_none()

        if usuario is not None:
            return usuario_schema.dump(Usuario)
        else:
            abort(404, "Person with last name {lname} not found")
class vistaCrearUsuario(Resource):
    def post(Usuario):
        lname = Usuario.get("lname","email")
        existing_usuario = Usuario.query.filter(new_usuario.lname == lname).one_or_none()

        if existing_usuario is None:
            new_usuario = usuario_schema.load(Usuario, session=db.session)
            db.session.add(new_usuario)
            db.session.commit()
            return usuario_schema.dump(new_usuario), 201
        else:
            abort(406,  "Person with last name {lname} already exists")
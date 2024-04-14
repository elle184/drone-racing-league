# usuario.py

# Remove: from datetime import datetime
from flask import make_response, abort

from config import db
from models import Usuario, usuario_schema, usuario_schema

def get(lname,email):
    usuario = Usuario.query.filter(Usuario.lname == lname).one_or_none()

    if person is not None:
        return usuario_schema.dump(Usuario)
    else:
        abort(404, f"Person with last name {lname} not found")
@jwt_required()
def post(usuario):
    lname = Usuario.get("lname","email")
    existing_usuario = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_usuario = usuario_schema.load(person, session=db.session)
        db.session.add(new_usuario)
        db.session.commit()
        return usuario_schema.dump(new_person), 201
    else:
        abort(406,  "Person with last name {lname} already exists")
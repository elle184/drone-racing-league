# modelo.py
from datetime import datetime
from modelo import db, ma
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db= SQLAlchemy()

class Usuario(db.Model):

    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    email= db.Column(db.String(32))
    contraseña = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow

    )

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        sqla_session = db.session

usuario_schema = UsuarioSchema()
people_schema = UsuarioSchema(many=True)

class Tarea(db.Model):
    __tablename__ = "tarea"

    id = db.Column(db.Integer, primary_key=True)
    file=db.Column(db.Blob)
    fecha = db.Column(db.String(32))
    status= db.Column(db.String(32))

class TareaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        load_instance = True
        sqla_session = db.session

tarea_schema = TareaSchema()
tarea_schema = TareaSchema(many=True)
    

    



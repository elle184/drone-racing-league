# modelo.py
from datetime import datetime
from config import db, ma


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



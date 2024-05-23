import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class User(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    user = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.id, self.name, self.user, self.email)

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        # sqla_session = db.session

usuario_schema = UsuarioSchema()

class Video(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    path = db.Column(db.String(500))
    image = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Task(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    status = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
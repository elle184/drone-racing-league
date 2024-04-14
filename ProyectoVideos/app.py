from ProyectoVideos import create_app
from .modelo import *
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from .vistas import VistaLogin,VistaPermisos,VistaEventos

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

CORS(
        app,
        origins="*",
    )

api = Api(app)
api.add_resource(VistaLogin,'/Api/auth/login')
api.add_resource(VistaCrearUsuario,'Api/auth/signup')


jwt = JWTManager(app)
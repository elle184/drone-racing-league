from rest import create_app
from flask_restful import Api
from .vistas import VistaEjemplo

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaEjemplo, '/welcome')
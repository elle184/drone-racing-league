from rest import create_app
from flask_restful import Api
from .modelos import db, User
from .vistas import VistaEjemplo, VistaCrearUsuario, VistaLogin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)

# with app.app_context() :
#     user = User(name='Katie Rogers', password='Zaengie4y', user='Werly1957', email='KatieVRogers@superrito.com')
#     db.session.add(user)
#     db.session.commit()
#     print(User.query.all())

api = Api(app)
api.add_resource(VistaEjemplo, '/welcome')
api.add_resource(VistaCrearUsuario,'/api/auth/signup')
api.add_resource(VistaLogin, '/api/auth/login')
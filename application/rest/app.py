from rest import create_app
from flask_restful import Api
from .modelos import db, User
from .vistas import VistaEjemplo, UserView, LoginView, TaskView, TaskViewDetail

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
api.add_resource(UserView, '/api/auth/signup')
api.add_resource(LoginView, '/api/auth/login')
api.add_resource(TaskView, '/api/tasks')
api.add_resource(TaskViewDetail, '/api/tasks/<int:task_id>')

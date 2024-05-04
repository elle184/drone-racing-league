# tarea.py

# Remove: from datetime import datetime
from flask import make_response, abort
from flask_restful import Resource
from modelo import db
from modelo import Tarea, tarea_schema, TareaSchema
class VistaTareaAll(Resource):
    def getTareas():
        
         tareas= Tarea.query.all()
         if tareas is not None:
            return tarea_schema(many=True).jsonify(tareas)
         else:
            abort(404, "No existen registros de tareas")


class VistaTarea(Resource):
    def getTarea(idTarea):
        
        

class VistaCrearTareas(Resource):
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
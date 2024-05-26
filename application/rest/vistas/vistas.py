import datetime
from ..modelos import db, User, Task, Video, usuario_schema
from flask_restful import Resource
from flask import request, abort, jsonify
from flask_jwt_extended import create_access_token

from ..service.user_service import UserService
from ..util import token_util

class VistaEjemplo(Resource) :

    def get(self):
        return "Hello, World!"

class UserView(Resource):
    def post(self):
        try :
            if None != request.json :
                user = User(
                    password = request.json['password']
                    , user = request.json['username']
                    , email = request.json['email']
                )

                db.session.add(user)
                db.session.commit()
                return usuario_schema.dump(user), 201
        except Exception :
            abort(406, "Person already exists")

class LoginView(Resource):
    def post(self):
        user = User.query.filter(
            User.user == request.json['username']
            , User.password == request.json['password']).first()

        if user is not None:
            access_token = create_access_token(identity = user.id)
            return {"message" : "Inicio de sesión exitoso", "token" : access_token}
        else:
            abort(404, f"Person with last name {request.json['username']} not found")

class TaskView(Resource) :
    def get(self) :
        tasks = []
        user_service = UserService()
        decode_token = token_util.decode(request.headers['Authorization'].split(" ")[1])
        user = user_service.getById(decode_token['sub'])

        if user is not None :
            tasks = Task.query.all()

        return jsonify([{"id": task.id, "name": task.name, "video_id": task.video_id, "status": task.status} for task in tasks])

    def post(self):
        if request.json['filename'] is not None :
            user_service = UserService()
            decode_token = token_util.decode(request.headers['Authorization'].split(" ")[1])
            user = user_service.getById(decode_token['sub'])

            video = Video(
                name = request.json['filename']
                , path = '/home/lucka/Videos/drl-videos'
                , user_id = user.id)

            db.session.add(video)
            db.session.commit()

            task = Task(
                video_id = video.id
                , user_id = user.id
                , status = 'uploaded')

            db.session.add(task)
            db.session.commit()

class TaskViewDetail(Resource) :
    def get(self, task_id):
        task = None
        user_service = UserService()
        decode_token = token_util.decode(request.headers['Authorization'].split(" ")[1])
        user = user_service.getById(decode_token['sub'])

        if user is not None :
            task = Task.query.filter(Task.id == task_id).first()

        return jsonify({
            "id": task.id
            , "name": task.name
            , "status": task.status
            , "url" : f'http://localhost:5050/videos/{task.video_id}'})

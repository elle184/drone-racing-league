from flask_restful import Resource
from flask import Request

class VistaEjemplo(Resource) :

    def get(self):
        return "Hello, World!"
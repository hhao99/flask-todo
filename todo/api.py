from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for


api_bp = Blueprint('api',__name__)
api = Api(api_bp)

Todos = [
    {'task':'1st task', 'isdone': False },
    {'task':'2nd task', 'isdone': False },
    {'task':'3rd task', 'isdone': False },
    
    ]
class Todo(Resource):
    def get(self,id):
        id = int(id)
        return Todos[id]
class TodoList(Resource):
    def get(self):
        return Todos
       

api.add_resource(Todo,'/todo/<id>')
api.add_resource(TodoList,'/todo')

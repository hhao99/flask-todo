from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      task = db.Column(db.String(120))
      isDone= db.Column(db.Boolean)

      def __repr__(self):
            return f'<Todo> {self.task}'
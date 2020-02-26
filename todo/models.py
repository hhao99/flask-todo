
from todo import db

Class Todo(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      task = db.Column(db.String(120))
      isDone= db.Column(db.Boolean)

      def __repr__(self):
            return f'<Todo> {self.task}'
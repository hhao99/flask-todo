from flask import (
    render_template, redirect, render_template, 
    request, g, flash, url_for
)
from .forms import TodoForm
from .models import Todo
from .models import db


def init_route(app):

    @app.route('/')
    def index():
        
        todos = Todo.query.all()
        
        return render_template('index.html',todos = todos)

    @app.route('/new',methods=['GET','POST'])
    def new():
        if request.method == 'POST':
            form = TodoForm()
            print(form)
            if form.validate_on_submit():
                task = form.task.data 
                isDone = form.isDone.data
                t = Todo(task=task,isDone = isDone)
                print(t.isDone)
                db.session.add(t)
                db.session.commit()
                
                return redirect(url_for('index'))
        form = TodoForm()
        return render_template('edit.html',form=form,action=url_for('new'))

    @app.route('/delete/<int:id>')
    def delete(id):
        print(f"delete the todo with id: {id}")
        todo = db.session.query(Todo).get(id)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))
    @app.route('/update/<int:id>')
    def update(id):
        print(f"update the todo with id: {id}")
        todo = db.session.query(Todo).get(id)
        todo.isDone = not todo.isDone
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
       
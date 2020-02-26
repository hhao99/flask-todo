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
            if form.validate_on_submit():
                task = form.task.data 
                isDone = form.isdone.data
                t = Todo(task=task,isDone = isDone)
                print(t)
                db.session.add(t)
                db.commit()
                print(t + " is saved")
                return redirect(url_for('index'))
        form = TodoForm()
        return render_template('edit.html',form=form,action=url_for('new'))

    @app.route('/delete/<int:id>')
    def delete(id):
        del todos[id]
        return redirect(url_for('index'))
       
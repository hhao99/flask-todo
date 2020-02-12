from flask import (
    render_template, redirect, render_template, 
    request, g, flash, url_for
)

todos = []
def init_route(app):

    @app.route('/')
    def index():
        
        return render_template('index.html',todos = todos)

    @app.route('/new',methods=['GET','POST'])
    def new():
        if request.method == 'POST':
            form = TodoForm()
            if form.validate_on_submit():
                task = form.task.data 
                isDone = form.isdone.data
                todos.append({'task': task, 'isDone': isDone})
                return redirect(url_for('index'))
        form = TodoForm()
        return render_template('edit.html',form=form)

    @app.route('/delete/<int:id>')
    def delete(id):
        del todos[id]
        return redirect(url_for('index'))
       
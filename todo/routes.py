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
            task = request.form['task']
            todos.append({'task': task, 'isDone': False})
            return redirect(url_for('index'))
        return render_template('edit.html')
from flask import render_template, render_template, request, g, flash

def init_route(app):

    @app.route('/')
    def index():
        return render_template('index.html')
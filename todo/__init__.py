import os
from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path,'todo.sqlite3')
    )

    if(test_config == None):
        app.config.from_pyfile('../config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.mkdir(app.instance_path)
    except OSError:
        print("error create app dir")
    
    @app.route('/')
    def index():
        return "HOME"

    return app
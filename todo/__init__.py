import os
from flask import Flask
from flask_migrate import Migrate

from .api import api_bp


def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config=True)
    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
   

    # if(test_config == None):
    #     app.config.from_pyfile('../config.py',silent=True)
    # else:
    #     app.config.from_mapping(test_config)
    
    try:
        os.mkdir(app.instance_path)
    except OSError:
        print("error create app dir")
    
    
    from todo import models, routes

    models.db.init_app(app)
    migrate = Migrate(app,models.db)


    routes.init_route(app)

    app.register_blueprint(api_bp)

    return app
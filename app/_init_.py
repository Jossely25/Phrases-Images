from flask import Flask
import os
from .config import Config
from tasks.scheduler import scheduler  

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app.config.from_object(Config)

    app.secret_key = os.urandom(24)

    from routes.register import bp
    app.register_blueprint(bp)

    return app

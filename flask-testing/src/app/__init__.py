from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    with app.app_context():
        app.register_blueprint(main)
        return app
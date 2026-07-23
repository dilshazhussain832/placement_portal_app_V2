from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.routes import main
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

# Import the models package AFTER db is created
import app.models


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app
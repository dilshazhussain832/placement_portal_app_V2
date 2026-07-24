from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

from app.routes import main
from app.routes.auth import auth
from app.routes.admin import admin
import app.models


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:5173"]
    )

    

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(admin, url_prefix="/api/admin")

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_caching import Cache

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()




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
    cache.init_app(app)


    from app.routes import main
    from app.routes.auth import auth
    from app.routes.admin import admin
    from app.routes.company import company
    from app.routes.student import student

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/api")
    app.register_blueprint(admin, url_prefix="/api/admin")
    app.register_blueprint(company, url_prefix="/api/company")
    app.register_blueprint(student, url_prefix="/api/student")

    return app
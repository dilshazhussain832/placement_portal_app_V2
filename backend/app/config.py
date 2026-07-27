import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "mad2-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "..", "instance", "placement_portal.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = False

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
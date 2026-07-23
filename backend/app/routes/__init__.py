from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return {
        "message": "Placement Portal Backend is Running Successfully!"
    }
from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/login")
def home():
    return {
        "message": "Placement Portal Backend is Running Successfully!"
    }
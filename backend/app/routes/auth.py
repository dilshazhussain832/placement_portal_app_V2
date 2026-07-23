from flask import Blueprint, jsonify, request
from app import db
from app.models import User, Student


auth = Blueprint("auth", __name__)


@auth.route("/test")
def test():
    return jsonify({
        "message": "Authentication API is working!"
    })

@auth.route("/student/register", methods=["POST"])
def student_register():

    data = request.get_json()

    email = data.get("email")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        email=email,
        role="student"
    )

    user.set_password(data.get("password"))

    db.session.add(user)
    db.session.flush()

    student = Student(
        user_id=user.id,
        full_name=data.get("full_name"),
        phone=data.get("phone"),
        branch=data.get("branch"),
        cgpa=data.get("cgpa"),
        passing_year=data.get("passing_year"),
        skills=data.get("skills"),
        resume=""
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "message": "Student registered successfully"
    }), 201
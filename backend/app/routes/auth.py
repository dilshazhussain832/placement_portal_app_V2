from flask import Blueprint, jsonify, request
from app import db
from app.models import User, Student, Company
from flask import session


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

@auth.route("/company/register", methods=["POST"])
def company_register():

    data = request.get_json()

    email = data.get("email")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        email=email,
        role="company"
    )

    user.set_password(data.get("password"))

    db.session.add(user)
    db.session.flush()

    company = Company(
        user_id=user.id,
        company_name=data.get("company_name"),
        industry=data.get("industry"),
        website=data.get("website"),
        hr_name=data.get("hr_name"),
        hr_email=data.get("hr_email")
    )

    db.session.add(company)
    db.session.commit()

    return jsonify({
        "message": "Company registered successfully. Waiting for admin approval."
    }), 201

@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    if not user.check_password(password):
        return jsonify({"message": "Invalid email or password"}), 401

    if user.role == "company":
        company = Company.query.filter_by(user_id=user.id).first()

        if company.approval_status != "Approved":
            return jsonify({
                "message": "Company account is waiting for admin approval."
            }), 403

    session["user_id"] = user.id
    session["role"] = user.role

    return jsonify({
        "message": "Login successful",
        "role": user.role
    }), 200
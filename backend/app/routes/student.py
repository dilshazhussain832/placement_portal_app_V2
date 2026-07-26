from flask import Blueprint, jsonify, session, request
from app.models import Student, PlacementDrive, Company, Application
from app import db

student = Blueprint("student", __name__)

@student.route("/drives", methods=["GET"])
def get_available_drives():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    drives = PlacementDrive.query.filter_by(
        approval_status="Approved",
        status="Open"
    ).all()

    result = []

    for drive in drives:

        company = Company.query.get(drive.company_id)

        result.append({
            "id": drive.id,
            "company_name": company.company_name if company else "N/A",
            "job_title": drive.job_title,
            "job_description": drive.job_description,
            "eligibility": drive.eligibility,
            "salary": drive.salary,
            "application_deadline": str(drive.application_deadline)
        })

    return jsonify(result)

@student.route("/apply/<int:drive_id>", methods=["POST"])
def apply_for_drive(drive_id):

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    drive = PlacementDrive.query.filter_by(
        id=drive_id,
        approval_status="Approved",
        status="Open"
    ).first()

    if not drive:
        return jsonify({
            "message": "Placement drive not available"
        }), 404

    existing_application = Application.query.filter_by(
        student_id=student.id,
        drive_id=drive.id
    ).first()

    if existing_application:
        return jsonify({
            "message": "You have already applied for this drive."
        }), 400

    application = Application(
        student_id=student.id,
        drive_id=drive.id
    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "message": "Application submitted successfully."
    }), 201

@student.route("/applications", methods=["GET"])
def get_my_applications():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    applications = Application.query.filter_by(
        student_id=student.id
    ).all()

    result = []

    for application in applications:

        drive = PlacementDrive.query.get(application.drive_id)

        company = Company.query.get(drive.company_id)

        result.append({
            "application_id": application.id,
            "drive_id": drive.id,
            "company_name": company.company_name,
            "job_title": drive.job_title,
            "application_date": str(application.application_date.date()),
            "status": application.status
        })

    return jsonify(result)

@student.route("/profile", methods=["GET"])
def get_profile():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    return jsonify({
        "full_name": student.full_name,
        "phone": student.phone,
        "branch": student.branch,
        "cgpa": student.cgpa,
        "passing_year": student.passing_year,
        "skills": student.skills
    })

@student.route("/profile", methods=["PUT"])
def update_profile():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.get_json()

    student.full_name = data["full_name"]
    student.phone = data["phone"]
    student.branch = data["branch"]
    student.cgpa = data["cgpa"]
    student.passing_year = data["passing_year"]
    student.skills = data["skills"]

    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully."
    })
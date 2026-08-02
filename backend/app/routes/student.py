from flask import Blueprint, jsonify, session, request, current_app, send_from_directory
from app.models import Student, PlacementDrive, Company, Application
from app import db
from werkzeug.utils import secure_filename
import os

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

    if not student.user.is_active:
        return jsonify({
            "message": "Your account has been deactivated by the administrator."
        }), 403

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
            "status": application.status,
            "interview_date": application.interview_date,
            "interview_time": str(application.interview_time) if application.interview_time else None,
            "interview_mode": application.interview_mode,
            "interview_location": application.interview_location,
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
        "skills": student.skills,
        "resume": student.resume
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

@student.route("/upload-resume", methods=["POST"])
def upload_resume():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    if "resume" not in request.files:
        return jsonify({"message": "No resume uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"message": "No file selected"}), 400

    filename = f"{student.id}_{secure_filename(file.filename)}"

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    student.resume = filename

    db.session.commit()

    return jsonify({
        "message": "Resume uploaded successfully.",
        "resume": filename
    })

@student.route("/resume", methods=["GET"])
def view_resume():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student or not student.resume:
        return jsonify({"message": "Resume not found"}), 404

    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],
        student.resume
    )

@student.route("/export-applications", methods=["POST"])
def export_my_applications():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    from app.services.tasks import export_student_applications

    export_student_applications.delay(student.id)

    return jsonify({
        "message": "Application export started successfully."
    })

@student.route("/download-applications", methods=["GET"])
def download_my_applications():

    if session.get("role") != "student":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not student:
        return jsonify({"message": "Student not found"}), 404

    filename = f"student_{student.id}_applications.csv"

    return send_from_directory(
        current_app.config["EXPORT_FOLDER"],
        filename,
        as_attachment=True
    )
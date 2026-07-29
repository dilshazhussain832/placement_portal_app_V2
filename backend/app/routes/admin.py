from flask import Blueprint, jsonify, session, request, send_from_directory, current_app, send_file
from app import db, cache
from app.models import User, Student, Company, PlacementDrive, Application
import os

admin = Blueprint("admin", __name__)

@admin.route("/dashboard")
@cache.cached(timeout=60)
def dashboard():

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    return jsonify({
        "total_students": Student.query.count(),
        "total_companies": Company.query.count(),
        "pending_companies": Company.query.filter_by(
            approval_status="Pending"
        ).count(),
        "total_drives": PlacementDrive.query.count(),
        "total_applications": Application.query.count()
    })

@admin.route("/companies")
def get_companies():

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    search = request.args.get("search", "").strip()

    query = Company.query

    if search:
        query = query.filter(
            (Company.company_name.ilike(f"%{search}%")) |
            (Company.industry.ilike(f"%{search}%")) |
            (Company.hr_name.ilike(f"%{search}%"))
        )

    companies = query.all()

    result = []

    for company in companies:
        result.append({
            "id": company.id,
            "company_name": company.company_name,
            "industry": company.industry,
            "website": company.website,
            "hr_name": company.hr_name,
            "hr_email": company.hr_email,
            "approval_status": company.approval_status,
            "is_active": company.is_active
        })

    return jsonify(result)

@admin.route("/students")
def get_students():

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    search = request.args.get("search", "").strip()

    query = Student.query

    if search:
        query = query.filter(
            (Student.full_name.ilike(f"%{search}%")) |
            (Student.branch.ilike(f"%{search}%")) |
            (Student.phone.ilike(f"%{search}%"))
        )

    students = query.all()

    result = []

    for student in students:

        result.append({
            "id": student.id,
            "full_name": student.full_name,
            "phone": student.phone,
            "branch": student.branch,
            "cgpa": student.cgpa,
            "passing_year": student.passing_year,
            "skills": student.skills,
            "resume": student.resume,
            "is_active": student.user.is_active
        })

    return jsonify(result)

@admin.route("/company/<int:company_id>/toggle-status", methods=["PUT"])
def toggle_company_status(company_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.get(company_id)

    if not company:
        return jsonify({"message": "Company not found"}), 404

    company.user.is_active = not company.user.is_active

    db.session.commit()

    return jsonify({
        "message": "Company status updated successfully.",
        "is_active": company.user.is_active
    }), 200

@admin.route("/company/<int:company_id>/approve", methods=["PUT"])
def approve_company(company_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.get(company_id)

    if not company:
        return jsonify({"message": "Company not found"}), 404

    company.approval_status = "Approved"

    db.session.commit()

    return jsonify({
        "message": "Company approved successfully"
    })

@admin.route("/company/<int:company_id>/reject", methods=["PUT"])
def reject_company(company_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.get(company_id)

    if not company:
        return jsonify({"message": "Company not found"}), 404

    company.approval_status = "Rejected"

    db.session.commit()

    return jsonify({
        "message": "Company rejected successfully"
    })

@admin.route("/student/<int:student_id>/toggle-status", methods=["PUT"])
def toggle_student_status(student_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.get(student_id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    student.user.is_active = not student.user.is_active

    db.session.commit()

    return jsonify({
        "message": "Student status updated successfully.",
        "is_active": student.user.is_active
    }), 200

@admin.route("/drives", methods=["GET"])
def get_all_drives():

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    drives = PlacementDrive.query.all()

    result = []

    for drive in drives:

        company = Company.query.get(drive.company_id)

        result.append({
            "id": drive.id,
            "company_name": company.company_name if company else "N/A",
            "job_title": drive.job_title,
            "salary": drive.salary,
            "application_deadline": str(drive.application_deadline),
            "status": drive.status,
            "approval_status": drive.approval_status
        })

    return jsonify(result)

@admin.route("/drive/<int:drive_id>/approve", methods=["PUT"])
def approve_drive(drive_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    drive = PlacementDrive.query.get(drive_id)

    if not drive:
        return jsonify({"message": "Placement drive not found"}), 404

    drive.approval_status = "Approved"

    db.session.commit()

    return jsonify({
        "message": "Placement drive approved successfully"
    })

@admin.route("/drive/<int:drive_id>/reject", methods=["PUT"])
def reject_drive(drive_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    drive = PlacementDrive.query.get(drive_id)

    if not drive:
        return jsonify({"message": "Placement drive not found"}), 404

    drive.approval_status = "Rejected"

    db.session.commit()

    return jsonify({
        "message": "Placement drive rejected successfully"
    })

@admin.route("/resume/<int:student_id>", methods=["GET"])
def view_student_resume(student_id):

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    student = Student.query.get(student_id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    if not student.resume:
        return jsonify({"message": "Resume not uploaded"}), 404

    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"],
        student.resume
    )

@admin.route("/export-students", methods=["POST"])
def export_students():

    from app.services.tasks import export_students_csv

    task = export_students_csv.delay()

    return {
        "message": "Student export started successfully.",
        "task_id": task.id
    }, 202


@admin.route("/download-students", methods=["GET"])
def download_students():

    export_folder = current_app.config["EXPORT_FOLDER"]

    file_path = os.path.join(export_folder, "students.csv")

    if not os.path.exists(file_path):
        return {
            "message": "Please export students first."
        }, 404

    return send_file(
        file_path,
        as_attachment=True,
        download_name="students.csv"
    )

@admin.route("/daily-reminder", methods=["POST"])
def run_daily_reminder():

    from app.services.tasks import daily_reminder

    task = daily_reminder.delay()

    return {
        "message": "Daily reminder task started.",
        "task_id": task.id
    }, 202

@admin.route("/monthly-report", methods=["POST"])
def run_monthly_report():

    if session.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 401

    from app.services.tasks import monthly_activity_report

    monthly_activity_report.delay()

    return jsonify({
        "message": "Monthly report started successfully."
    })
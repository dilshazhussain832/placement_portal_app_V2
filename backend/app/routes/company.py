from flask import Blueprint, jsonify, request, session, send_from_directory, current_app
from app import db
from app.models import Company, PlacementDrive, Student, Application, User
from datetime import datetime

company = Blueprint("company", __name__)

@company.route("/drive", methods=["POST"])
def create_drive():

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(user_id=session["user_id"]).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

    if not company.user.is_active:
        return jsonify({
            "message": "Your account has been deactivated by the administrator."
        }), 403

    data = request.get_json()

    drive = PlacementDrive(
        company_id=company.id,
        job_title=data.get("job_title"),
        job_description=data.get("job_description"),
        eligibility=data.get("eligibility"),
        salary=data.get("salary"),
        application_deadline=datetime.strptime(
            data.get("application_deadline"),
            "%Y-%m-%d"
        ).date()
    )

    db.session.add(drive)
    db.session.commit()

    return jsonify({
        "message": "Placement drive created successfully"
    }), 201

@company.route("/drives", methods=["GET"])
def get_company_drives():

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(user_id=session["user_id"]).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

    drives = PlacementDrive.query.filter_by(company_id=company.id).all()

    result = []

    for drive in drives:

        result.append({
            "id": drive.id,
            "job_title": drive.job_title,
            "eligibility": drive.eligibility,
            "salary": drive.salary,
            "application_deadline": str(drive.application_deadline),
            "status": drive.status,
            "job_description": drive.job_description,
            "approval_status": drive.approval_status
        })

    return jsonify(result)

@company.route("/drive/<int:drive_id>", methods=["PUT"])
def update_drive(drive_id):

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(user_id=session["user_id"]).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

    drive = PlacementDrive.query.filter_by(
        id=drive_id,
        company_id=company.id
    ).first()
    

    if not drive:
        return jsonify({"message": "Placement drive not found"}), 404

    if drive.approval_status == "Approved":
        return jsonify({
            "message": "Approved placement drives cannot be edited."
        }), 400

    data = request.get_json()

    drive.job_title = data.get("job_title", drive.job_title)
    drive.job_description = data.get(
        "job_description",
        drive.job_description
    )
    drive.eligibility = data.get(
        "eligibility",
        drive.eligibility
    )
    drive.salary = data.get(
        "salary",
        drive.salary
    )

    if data.get("application_deadline"):
        drive.application_deadline = datetime.strptime(
            data["application_deadline"],
            "%Y-%m-%d"
        ).date()

    db.session.commit()

    return jsonify({
        "message": "Placement drive updated successfully"
    })

@company.route("/drive/<int:drive_id>", methods=["DELETE"])
def delete_drive(drive_id):

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(user_id=session["user_id"]).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

    drive = PlacementDrive.query.filter_by(
        id=drive_id,
        company_id=company.id
    ).first()

    if not drive:
        return jsonify({"message": "Placement drive not found"}), 404

    if drive.approval_status == "Approved":
        return jsonify({
            "message": "Approved placement drives cannot be deleted."
        }), 400

    db.session.delete(drive)
    db.session.commit()

    return jsonify({
        "message": "Placement drive deleted successfully"
    })

@company.route("/drive/<int:drive_id>/toggle-status", methods=["PUT"])
def toggle_drive_status(drive_id):

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(user_id=session["user_id"]).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

    drive = PlacementDrive.query.filter_by(
        id=drive_id,
        company_id=company.id
    ).first()

    if not drive:
        return jsonify({"message": "Placement drive not found"}), 404

    if drive.approval_status == "Rejected":
        return jsonify({
            "message": "Rejected placement drives cannot be reopened or closed."
        }), 400

    if drive.status == "Open":
        drive.status = "Closed"
    else:
        drive.status = "Open"

    db.session.commit()

    return jsonify({
        "message": f"Drive is now {drive.status}",
        "status": drive.status
    })


@company.route("/drive/<int:drive_id>/applications", methods=["GET"])
def get_drive_applications(drive_id):

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

    drive = PlacementDrive.query.filter_by(
        id=drive_id,
        company_id=company.id
    ).first()

    if not drive:
        return jsonify({"message": "Placement drive not found"}), 404

    applications = Application.query.filter_by(
        drive_id=drive.id
    ).all()

    result = []

    for application in applications:

        student = Student.query.get(application.student_id)

        user = User.query.get(student.user_id)

        result.append({

            "application_id": application.id,

            "student_id": student.id,

            "student_name": student.full_name,

            "email": user.email,

            "phone": student.phone,

            "branch": student.branch,

            "cgpa": student.cgpa,

            "passing_year": student.passing_year,

            "skills": student.skills,

            "resume": student.resume,

            "status": application.status,

            "application_date": str(
                application.application_date.date()
            )

        })

    return jsonify(result)

@company.route("/application/<int:application_id>/shortlist", methods=["PUT"])
def shortlist_applicant(application_id):

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    application = Application.query.get(application_id)

    if not application:
        return jsonify({"message": "Application not found"}), 404

    drive = PlacementDrive.query.get(application.drive_id)

    company = Company.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if drive.company_id != company.id:
        return jsonify({"message": "Unauthorized"}), 403

    if application.status != "Applied":
        return jsonify({
            "message": "Final decision has already been made."
        }), 400

    application.status = "Shortlisted"

    db.session.commit()

    return jsonify({
        "message": "Applicant shortlisted successfully."
    })

@company.route("/application/<int:application_id>/reject", methods=["PUT"])
def reject_applicant(application_id):

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    application = Application.query.get(application_id)

    if not application:
        return jsonify({"message": "Application not found"}), 404

    drive = PlacementDrive.query.get(application.drive_id)

    company = Company.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if drive.company_id != company.id:
        return jsonify({"message": "Unauthorized"}), 403

    if application.status != "Applied":
        return jsonify({
            "message": "Final decision has already been made."
        }), 400

    application.status = "Rejected"

    db.session.commit()

    return jsonify({
        "message": "Applicant rejected successfully."
    })

@company.route("/profile", methods=["GET"])
def get_company_profile():

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company_data = Company.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not company_data:
        return jsonify({"message": "Company not found"}), 404

    return jsonify({
        "company_name": company_data.company_name,
        "industry": company_data.industry,
        "website": company_data.website,
        "hr_name": company_data.hr_name,
        "hr_email": company_data.hr_email
    })

@company.route("/profile", methods=["PUT"])
def update_company_profile():

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company_data = Company.query.filter_by(
        user_id=session["user_id"]
    ).first()

    if not company_data:
        return jsonify({"message": "Company not found"}), 404

    data = request.get_json()

    company_data.company_name = data["company_name"]
    company_data.industry = data["industry"]
    company_data.website = data["website"]
    company_data.hr_name = data["hr_name"]
    company_data.hr_email = data["hr_email"]

    db.session.commit()

    return jsonify({
        "message": "Company profile updated successfully."
    })

@company.route("/resume/<int:student_id>", methods=["GET"])
def view_student_resume(student_id):

    if session.get("role") != "company":
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
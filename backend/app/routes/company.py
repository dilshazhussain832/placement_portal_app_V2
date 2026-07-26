from flask import Blueprint, jsonify, request, session
from app import db
from app.models import Company, PlacementDrive
from datetime import datetime

company = Blueprint("company", __name__)

@company.route("/drive", methods=["POST"])
def create_drive():

    if session.get("role") != "company":
        return jsonify({"message": "Unauthorized"}), 401

    company = Company.query.filter_by(user_id=session["user_id"]).first()

    if not company:
        return jsonify({"message": "Company not found"}), 404

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

    if drive.status == "Open":
        drive.status = "Closed"
    else:
        drive.status = "Open"

    db.session.commit()

    return jsonify({
        "message": f"Drive is now {drive.status}",
        "status": drive.status
    })
from flask import Blueprint, jsonify, session
from app import db
from app.models import User, Student, Company, PlacementDrive, Application

admin = Blueprint("admin", __name__)

@admin.route("/dashboard")
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

    companies = Company.query.all()

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
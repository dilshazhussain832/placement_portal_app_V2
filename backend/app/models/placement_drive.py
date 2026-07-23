from app import db


class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

    job_title = db.Column(db.String(150), nullable=False)

    job_description = db.Column(db.Text, nullable=False)

    eligibility = db.Column(db.String(255), nullable=False)

    salary = db.Column(db.String(50))

    application_deadline = db.Column(db.Date, nullable=False)

    status = db.Column(db.String(20), default="Pending")

    applications = db.relationship("Application", backref="placement_drive", lazy=True)

    placements = db.relationship("Placement", backref="placement_drive", lazy=True)
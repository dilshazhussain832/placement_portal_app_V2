from datetime import datetime
from app import db


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)

    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drives.id"), nullable=False)

    application_date = db.Column(db.DateTime, default=datetime.utcnow)

    status = db.Column(db.String(20), default="Applied")

    interview_date = db.Column(db.Date, nullable=True)

    interview_time = db.Column(db.Time, nullable=True)

    interview_mode = db.Column(db.String(20), nullable=True)

    interview_location = db.Column(db.String(255), nullable=True)
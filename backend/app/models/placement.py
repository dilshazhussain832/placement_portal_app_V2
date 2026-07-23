from app import db


class Placement(db.Model):
    __tablename__ = "placements"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)

    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

    drive_id = db.Column(db.Integer, db.ForeignKey("placement_drives.id"), nullable=False)

    joining_date = db.Column(db.Date)

    package = db.Column(db.String(50))
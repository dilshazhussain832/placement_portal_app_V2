from app import db


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    company_name = db.Column(db.String(150), nullable=False)

    industry = db.Column(db.String(100), nullable=False)

    website = db.Column(db.String(255))

    hr_name = db.Column(db.String(100), nullable=False)

    hr_email = db.Column(db.String(120), nullable=False)

    approval_status = db.Column(db.String(20), default="Pending")
    is_active = db.Column(db.Boolean, default=True)
    placement_drives = db.relationship("PlacementDrive", backref="company", lazy=True)
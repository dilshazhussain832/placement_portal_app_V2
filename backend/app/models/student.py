from app import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    full_name = db.Column(db.String(100), nullable=False)

    phone = db.Column(db.String(15), nullable=False)

    branch = db.Column(db.String(100), nullable=False)

    cgpa = db.Column(db.Float, nullable=False)

    passing_year = db.Column(db.Integer, nullable=False)

    skills = db.Column(db.Text)

    resume = db.Column(db.String(255))

    approved = db.Column(db.Boolean, default=True)

    applications = db.relationship("Application", backref="student", lazy=True)

    placements = db.relationship("Placement", backref="student", lazy=True)
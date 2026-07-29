from app.services.celery_app import celery
from app.models.student import Student
from app.models.application import Application
from app.models.company import Company
from app.models.placement_drive import PlacementDrive
from app import create_app
import pandas as pd
import os
from app.services.email_service import send_email
from app.models.user import User

app = create_app()


@celery.task
def export_students_csv():

    with app.app_context():

        students = Student.query.all()

        data = []

        for student in students:

            data.append({
                "ID": student.id,
                "Full Name": student.full_name,
                "Phone": student.phone,
                "Branch": student.branch,
                "CGPA": student.cgpa,
                "Passing Year": student.passing_year,
                "Skills": student.skills,
                "Approved": student.approved
            })

        df = pd.DataFrame(data)

        export_folder = app.config["EXPORT_FOLDER"]

        os.makedirs(export_folder, exist_ok=True)

        file_path = os.path.join(export_folder, "students.csv")

        df.to_csv(file_path, index=False)

        return file_path


@celery.task
def export_student_applications(student_id):

    with app.app_context():

        applications = (
            Application.query
            .filter_by(student_id=student_id)
            .all()
        )

        data = []

        for application in applications:

            drive = PlacementDrive.query.get(application.drive_id)

            company = Company.query.get(drive.company_id)

            data.append({
                "Student ID": application.student_id,
                "Company Name": company.company_name,
                "Drive Title": drive.job_title,
                "Application Status": application.status,
                "Application Date": application.application_date.strftime("%Y-%m-%d %H:%M")
            })

        df = pd.DataFrame(data)

        export_folder = app.config["EXPORT_FOLDER"]

        os.makedirs(export_folder, exist_ok=True)

        file_path = os.path.join(
            export_folder,
            f"student_{student_id}_applications.csv"
        )

        df.to_csv(file_path, index=False)

        return file_path

from app.models.user import User
from app.services.email_service import send_email


@celery.task
def daily_reminder():

    with app.app_context():

        students = Student.query.all()

        for student in students:

            user = User.query.get(student.user_id)

            if not user or not user.email:
                continue

            send_email(
                to_email=user.email,
                subject="Placement Portal Daily Reminder",
                body=f"""Hello {student.full_name},

This is your daily reminder to check the Placement Portal.

New placement drives may have been posted and application deadlines may be approaching.

Log in and check the latest opportunities.

Regards,
Institute Placement Cell
"""
            )

    return "Daily Reminder Emails Sent"

@celery.task
def monthly_activity_report():

    with app.app_context():

        total_drives = PlacementDrive.query.count()

        total_applications = Application.query.count()

        total_selected = Application.query.filter_by(
            status="Selected"
        ).count()

        admin = User.query.filter_by(
            role="admin"
        ).first()

        if not admin:
            return "Admin not found"

        html = f"""
        <html>
        <body>

        <h2>Monthly Placement Activity Report</h2>

        <table border="1" cellpadding="8" cellspacing="0">

            <tr>
                <th>Statistic</th>
                <th>Value</th>
            </tr>

            <tr>
                <td>Total Placement Drives</td>
                <td>{total_drives}</td>
            </tr>

            <tr>
                <td>Total Applications</td>
                <td>{total_applications}</td>
            </tr>

            <tr>
                <td>Total Selected Students</td>
                <td>{total_selected}</td>
            </tr>

        </table>

        <br>

        <p>
            This report was generated automatically by the
            Placement Portal.
        </p>

        </body>
        </html>
        """

        send_email(
            to_email=admin.email,
            subject="Monthly Placement Activity Report",
            body=html
        )

    return "Monthly Report Sent"
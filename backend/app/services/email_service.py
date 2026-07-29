import smtplib

from email.mime.text import MIMEText

from flask import current_app


def send_email(to_email, subject, body):

    msg = MIMEText(body, "html")

    msg["Subject"] = subject
    msg["From"] = current_app.config["MAIL_USERNAME"]
    msg["To"] = to_email

    server = smtplib.SMTP(
        current_app.config["MAIL_SERVER"],
        current_app.config["MAIL_PORT"]
    )

    server.starttls()

    server.login(
        current_app.config["MAIL_USERNAME"],
        current_app.config["MAIL_PASSWORD"]
    )

    server.send_message(msg)

    server.quit()
import os
from dotenv import load_dotenv

from app import create_app, db
from app.models import User

# Load variables from .env
load_dotenv()

app = create_app()

with app.app_context():

    admin = User.query.filter_by(role="admin").first()

    if not admin:

        admin = User(
            email=os.getenv("ADMIN_EMAIL"),
            role="admin"
        )

        admin.set_password(
            os.getenv("ADMIN_PASSWORD")
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully!")

    else:

        admin.email = os.getenv("ADMIN_EMAIL")

        db.session.commit()

        print("Admin email updated successfully!")
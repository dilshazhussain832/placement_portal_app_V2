from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    admin = User.query.filter_by(email="admin@placement.com").first()

    if not admin:
        admin = User(
            email="admin@placement.com",
            password="admin123",
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created successfully!")
    else:
        print("Admin already exists!")
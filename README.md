# 🎓 Placement Portal Application (PPA) - Version 2

## 📖 Overview

Brief description of the project.

---

## 🚀 Features

### 👨‍🎓 Student
- Register & Login
- Update Profile
- Upload Resume
- Search Placement Drives
- Apply for Placement Drives
- Track Application Status
- Export Application History

### 🏢 Company
- Register (Admin Approval Required)
- Create & Manage Placement Drives
- View Applicants
- Shortlist / Reject Students
- Schedule Interviews
- Update Final Selection Status

### 🛡 Admin
- Dashboard Statistics
- Approve / Reject Companies
- Approve / Reject Placement Drives
- Search Students & Companies
- Blacklist / Activate Accounts
- View All Applications
- Export Students CSV
- Run Daily Reminder & Monthly Report

---

## 🛠 Tech Stack

### Frontend
- Vue.js 3
- Vue Router
- Bootstrap 5

### Backend
- Flask
- SQLAlchemy

### Database
- SQLite

### Background Jobs
- Redis
- Celery
- Celery Beat

### Other Libraries
- Flask-Mail
- Flask-Caching
- Python Dotenv

---

## ⚙️ Prerequisites

- Python 3.11+
- Node.js & npm
- Redis Server
- Git (Optional)

---

## 📦 Installation

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Frontend

```bash
cd frontend

npm install
```

---

## 🔐 Environment Variables

Create a `.env` file inside the backend folder.

Example:

```env
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_DEFAULT_SENDER=your_email@gmail.com
```

---

## ▶️ Running the Project

### 1. Start Redis

```bash
redis-server
```

### 2. Start Flask Backend

```bash
cd backend

venv\Scripts\activate

python run.py
```

### 3. Start Celery Worker

```bash
cd backend

venv\Scripts\activate

celery -A app.services.celery_app:celery worker -P solo -l info
```

### 4. Start Celery Beat

```bash
cd backend

venv\Scripts\activate

celery -A app.services.celery_app:celery beat -l info
```

### 5. Start Vue Frontend

```bash
cd frontend

npm run dev
```

---

## 🌐 Application URLs

| Service | URL |
|----------|-----|
| Homepage | http://localhost:5173/home |
| Login | http://localhost:5173/login |
| Backend API | http://127.0.0.1:5000 |

---

## 👤 Default Admin Account

Admin account is created automatically during database initialization.


```text
Email: dilshazhussain123@gmail.com
Password: admin123
```

---

## 🗄 Database

- SQLite Database
- SQLAlchemy ORM
- Database is created automatically on first run.

---

## 📁 Project Structure

```text
Placement-Portal/
│
├── backend/
├── frontend/
├── README.md
└── project report
```

---

## 📌 Important Notes

- Redis must be running before starting Celery Worker and Celery Beat.
- Company accounts require Admin approval before login.
- Blacklisted users cannot log in.
- Database tables are created automatically.
- Celery is used for CSV export, daily reminders, and monthly reports.

---

## 👨‍💻 Author

**Dilshaz Hussain**

IIT Madras BS Degree Program

Modern Application Development II (MAD-2)
from celery import Celery
from celery.schedules import crontab
from app import create_app


flask_app = create_app()

celery = Celery(
    flask_app.import_name,
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.update(flask_app.config)

celery.conf.beat_schedule = {
    "daily-reminder": {
        "task": "app.services.tasks.daily_reminder",
        "schedule": crontab(hour=18, minute=0),
    },

    "monthly-activity-report": {
        "task": "app.services.tasks.monthly_activity_report",
        "schedule": crontab(
            day_of_month=1,
            hour=9,
            minute=0
        ),
    },
}


class ContextTask(celery.Task):

    def __call__(self, *args, **kwargs):

        with flask_app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask

import app.services.tasks
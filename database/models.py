from database.db import db
from datetime import datetime

class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)

    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    processing_time = db.Column(db.DateTime, nullable=True)
    completed_time = db.Column(db.DateTime, nullable=True)

    status = db.Column(db.String(20), default="started")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "processing_time": self.processing_time.isoformat() if self.processing_time else None,
            "completed_time": self.completed_time.isoformat() if self.completed_time else None,
            "status": self.status
        }

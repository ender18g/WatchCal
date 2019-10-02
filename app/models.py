from app import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(256), index=True)
    password_hash = db.Column(db.String(128))
    points = db.Column(db.Integer, default=0, index=True)
    qualification = db.Column(db.String(128), default="None")
    scheduled_days = db.relationship('Schedule', backref="duty_stander", lazy='dynamic')

    def __repr__(self):
        return f"User: {self.email}"


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, index=True, unique=True)
    value = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True, nullable=True)

    def __repr__(self):
        return f"Day: {self.date}"


# local import
from app import db, datetime

class TimestampModel():
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=True, onupdate=datetime.utcnow)
    deleted_date = db.Column(db.DateTime, nullable=True)

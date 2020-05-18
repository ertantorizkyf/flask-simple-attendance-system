# local import
from app.models import db

class AttendanceModel(db.Model):
    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_in = db.Column(db.DateTime, nullable=False)
    time_out = db.Column(db.DateTime, nullable=True)

    # Relationship
    user = db.relationship('UserModel', back_populates='attendances')
    

    @classmethod
    def get_recent_by_user_id(cls, user_id):
        return cls.query.filter(cls.user_id == user_id).order_by(cls.id.desc()).first()
    
    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter(cls.user_id == user_id).order_by(cls.id.desc()).all()
    
    def insert(self):
        db.session.add(self)
        db.session.flush()

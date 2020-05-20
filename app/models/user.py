# package import
import hashlib
import bcrypt

# local import
from app.models import db, datetime, UserMixin
from app.models.timestamp import TimestampModel

class UserModel(UserMixin, db.Model, TimestampModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    last_login_date = db.Column(db.DateTime, nullable=True)

    # Relationship
    attendances = db.relationship('AttendanceModel', back_populates='user')
    

    @classmethod
    def get_all(cls):
        return cls.query.filter(cls.deleted_date == None).all()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter(cls.email == email, cls.deleted_date == None).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.id == id, cls.deleted_date == None).first()
    
    def insert(self):
        db.session.add(self)
        db.session.flush()

    def delete(self):
        self.deleted_date = datetime.utcnow().isoformat()

    def check_password(self, password):
        raw_password = hashlib.sha256(password.encode()).hexdigest()
        is_password_match = bcrypt.checkpw(raw_password.encode(), self.password.encode())

        if is_password_match:
            return True

        return False

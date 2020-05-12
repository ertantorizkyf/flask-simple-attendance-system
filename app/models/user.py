# package import
from werkzeug.security import generate_password_hash, check_password_hash

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
    

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter(cls.email == email).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.id == id).first()
    
    def insert(self):
        db.session.add(self)
        db.session.flush()

    def delete(self):
        self.deleted_at = datetime.utcnow().isoformat()

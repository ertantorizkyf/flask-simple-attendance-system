# package import
import hashlib
import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

# local import
from app import db
from app.models.user import UserModel
from app.helpers import auth
from instance.config import ADMIN_PASSWORD

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        
        # check whether password is correct
        user = UserModel.get_by_email(email)
        if user:
            check_password = user.check_password(password)

            if check_password:
                login_user(user)
                return redirect('/')
            
            return 'Password doesn\'t match'

        return 'Email not registered'

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_bp.login'))

@user_bp.route('/')
@login_required
def index():
    return render_template('index.html', current_user=current_user)

@user_bp.route('/user/create-admin')
def create_admin():
    raw_password = hashlib.sha256(ADMIN_PASSWORD.encode()).hexdigest()
    hashed_password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt())

    admin = UserModel(
        name = 'admin',
        email = 'admin@mail.com',
        password = hashed_password,
        is_admin = True
    )

    try:
        admin.insert()
        db.session.commit()
    except:
        db.session.rollback()
        return 'Error while inserting admin'
    
    return 'Admin created'

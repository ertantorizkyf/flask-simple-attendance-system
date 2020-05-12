# package import
from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, login_required, current_user, login_user, logout_user

# local import
from app import db
from app.models.user import User
from app.helpers import auth

# @login_manager.request_loader
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login')
def login():
    return 'OK'

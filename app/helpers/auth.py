from flask import redirect

from app import login_manager
from app.models.user import User

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.get_by_id(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

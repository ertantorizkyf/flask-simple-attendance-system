from app.controllers.user import user_bp
from app.controllers.attendance import attendance_bp

def register_blueprints(app):
    # register all blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(attendance_bp)

    return app

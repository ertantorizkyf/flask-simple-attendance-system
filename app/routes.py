from app.controllers.user import user_bp

def register_blueprints(app):
    # register all blueprints
    app.register_blueprint(user_bp)

    return app

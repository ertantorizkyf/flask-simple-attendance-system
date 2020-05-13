# package import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

# file import
from config import app_config

# init sqlalchemy
db = SQLAlchemy()

# init login
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    login_manager.init_app(app)

    with app.app_context():
        # register all blueprints
        from app import routes

        routes.register_blueprints(app)
        
        return app

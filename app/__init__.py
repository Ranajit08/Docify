from flask import Flask
from .extensions import db, migrate
from .routes.index import main_bp
from .routes.auth import auth_bp
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='docify',
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, 'db.sqlite3'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    try:
        os.makedirs(app.instance_path)
        storage = os.path.join(app.instance_path, "storage", "users")
        os.makedirs(storage, exist_ok = True)
    except OSError:
        pass
    
    db.init_app(app)
    migrate.init_app(app, db)
    from .models import user, file
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
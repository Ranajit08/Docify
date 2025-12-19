from flask import Flask
from .extensions import db, migrate
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='docify',
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(app.instance_path, 'db.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    try:
        os.makedirs(app.instance_path)
        os.makedirs("storage", exist_ok = True)
        os.makedirs("storage/users", exist_ok = True)
    except OSError:
        pass
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    @app.route("/")
    def home():
        return "hello World from gargi"
    
    # register blueprints

    return app
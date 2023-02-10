from flask import Flask

from .database import db
from .views import main
from .utils import make_celery

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SECRET_KEY"] = "root"
    app.config["CELERY_CONFIG"] = {"broker_url": "redis://redis", "result_backend": "redis://redis"}

    db.init_app(app)

    celery = make_celery(app)
    celery.set_default()

    app.register_blueprint(main)

    return app, celery

from src import models

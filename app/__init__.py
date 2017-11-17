from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from raven.contrib.flask import Sentry
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension()
sentry = Sentry(dsn="https://f2010cadf0ef406f8e108f3e396e83b5:55471c2c8cc043f1a3d066f1a72f83de@sentry.io/246585")

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.default")
    app.config.from_pyfile("config.py")
    app.config.from_envvar("APP_CONFIG_FILE")
    db.init_app(app)
    toolbar.init_app(app)
    sentry.init_app(app)
    if app.config["DEBUG"]:
        from werkzeug import SharedDataMiddleware
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/": os.path.join(os.path.dirname(__file__), "static")
        })
    bcrypt.init_app(app)

    from .api.views.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .api.views.base import base_blueprint
    app.register_blueprint(base_blueprint)
    from .api.views.trade import trades_blueprint
    app.register_blueprint(trades_blueprint)
    from .api.views.user import users_blueprint
    app.register_blueprint(users_blueprint)

    from app.api.models import user, trade

    return app

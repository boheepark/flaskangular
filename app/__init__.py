from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension()

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS"))
    db.init_app(app)
    toolbar.init_app(app)
    if app.config["DEBUG"]:
        from werkzeug import SharedDataMiddleware
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/": os.path.join(os.path.dirname(__file__), "static")
        })
    bcrypt.init_app(app)

    from app.api.views.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    from app.api.views.base import base_blueprint
    app.register_blueprint(base_blueprint)
    from app.api.views.trade import trades_blueprint
    app.register_blueprint(trades_blueprint)
    from app.api.views.user import users_blueprint
    app.register_blueprint(users_blueprint)

    from app.api.models import user, trade
    # from app.api.views import base, auth, user, trade

    return app

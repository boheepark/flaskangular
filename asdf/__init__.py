from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    db.init_app(app)
    if app.config["DEBUG"]:
        from werkzeug import SharedDataMiddleware
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/": os.path.join(os.path.dirname(__file__), "static")
        })
    from flask_bcrypt import Bcrypt
    bcrypt = Bcrypt(app)

    from asdf.api.views.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)
    from asdf.api.views.base import base_blueprint
    app.register_blueprint(base_blueprint)
    from asdf.api.views.trade import trades_blueprint
    app.register_blueprint(trades_blueprint)
    from asdf.api.views.user import users_blueprint
    app.register_blueprint(users_blueprint)

    from asdf.api.models import user, trade
    from asdf.api.views import base, auth, user, trade

    return app

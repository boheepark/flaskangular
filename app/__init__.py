import os

from flask import Flask
from flask_assets import Environment
from flask_bcrypt import Bcrypt
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

from .util.assets import bundles

cache = Cache(config={"CACHE_TYPE": "simple"})
db = SQLAlchemy()
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension()
sentry = Sentry(dsn="https://f2010cadf0ef406f8e108f3e396e83b5:55471c2c8cc043f1a3d066f1a72f83de@sentry.io/246585")

def create_app():
    app = Flask(__name__, instance_relative_config=True, static_folder="static")
    app.config.from_object("config.default")
    app.config.from_envvar("APP_CONFIG_FILE")
    cache.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)
    sentry.init_app(app)
    if app.config["DEBUG"]:
        from werkzeug import SharedDataMiddleware
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/": os.path.join(os.path.dirname(__file__), "static")
        })
    bcrypt.init_app(app)

    from .base.views import base_blueprint
    app.register_blueprint(base_blueprint)
    from .home.views import home_blueprint
    app.register_blueprint(home_blueprint)
    from .auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .users.views import users_blueprint
    app.register_blueprint(users_blueprint)
    from .trades.views import trades_blueprint
    app.register_blueprint(trades_blueprint)

    assets = Environment(app)
    assets.register(bundles)

    from app.trades import models

    return app

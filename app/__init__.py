from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object("app.config.DevelopmentConfig")
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "asdf"
if app.config["DEBUG"]:
    from werkzeug import SharedDataMiddleware
    import os
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        "/": os.path.join(os.path.dirname(__file__), "static")
    })
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from app.models import user, trade
from app.views import base, auth, user, trade

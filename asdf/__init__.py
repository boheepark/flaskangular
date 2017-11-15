from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)
db = SQLAlchemy(app)
if app.config["DEBUG"]:
    from werkzeug import SharedDataMiddleware
    import os
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        "/": os.path.join(os.path.dirname(__file__), "static")
    })
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from asdf.models import user, trade
from asdf.views import base, auth, user, trade

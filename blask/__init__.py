from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from os import urandom

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blask.sqlite"
app.config["SECRET_KEY"] = urandom(16)
app.config["BASIC_AUTH_USERNAME"] = "admin"
app.config["BASIC_AUTH_PASSWORD"] = "passw0rd"
db = SQLAlchemy(app)
auth = BasicAuth(app)
from blask.main.views import blueprint
from blask.main.models import Post
from blask.admin.views import admin_blueprint
app.register_blueprint(blueprint)
app.register_blueprint(admin_blueprint)
# admin = Admin(app, "blask", template_mode="bootstrap4")
# admin.add_view(ModelView(Post, db.session))
with app.app_context():
    db.create_all()
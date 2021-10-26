from flask import Flask

from apps.index.view import index_bp
from apps.user.view import user_bp
from settings import Config
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from exts import db, bootstrap
from apps.user.model import *
from apps.article.model import Article


def create_app():
    app = Flask(__name__, template_folder='../templates/', static_folder='../static/')
    app.config.from_object(Config) 
    bootstrap.init_app(app=app)  # bootstrap
    m = Moment(app)
    db.init_app(app) # 数据库
    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)
    # app.register_blueprint(user_bp)
    print(app.url_map)
    return app

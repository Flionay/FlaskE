from flask import Flask,render_template,session,redirect,url_for,flash
from settings import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email

from exts import db
from apps.user.user import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates/', static_folder='../static/') # type:Flask
    app.config.from_object(Config) 
    bootstrap = Bootstrap(app)  # 将应用实例传给构造函数
    m = Moment(app)
    db.init_app(app) # 数据库

    app.register_blueprint(user_bp)
    # print(app.url_map)
    return app

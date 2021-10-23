from flask import Flask,render_template,session,redirect,url_for
from Config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)  # 将应用实例传给构造函数
m = Moment(app)

# 定义表单类
class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    email = StringField("Enter your email",validators=[Email()])
    submit = SubmitField('Submit')

@app.route("/")
def index():
    utc = datetime.utcnow()
    return render_template("index.html",current_time=utc)


@app.route("/user",methods=['get','post'])
def user():
    name = None
    email = None
    form = NameForm()
    if form.validate_on_submit(): # 如果通过验证
        name = form.name.data
        email = form.email.data
        form.name.data = ''  # 重制
        form.email.data = ''

    utc = datetime.utcnow()
    return render_template("user.html",current_time=utc,form=form,name=name,email=email)

@app.errorhandler(404)
def errorhandler(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

app.run()
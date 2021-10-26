from flask import Blueprint, request, render_template
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
from wtforms import TextField, StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo

from apps.user.model import User
from exts import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


class RegisterForm(FlaskForm):
    name = StringField("名字", validators=[DataRequired()])
    phone = StringField("手机", validators=[DataRequired()])
    email = StringField("email", validators=[Email()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo('repassword', message='Passwords must match')])
    repassword = PasswordField("再次确认密码", validators=[DataRequired()])
    accept_tos = BooleanField("我接受隐私条约", validators=[DataRequired()])
    submit = SubmitField("提交")


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # 创建实体对象
        user = User()
        user.username = form.name.data
        user.password = generate_password_hash(form.password.data)
        user.email = form.email.data
        user.phone = form.phone.data

        # 添加到数据库
        db.session.add(user)
        db.session.commit()

        return '注册成功'

    return render_template("user/register.html", form=form)


@user_bp.route("/login")
def login():
    return render_template("index.html")
from flask import Blueprint, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import TextField, StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo

from apps.user.model import User
from exts import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


class LoginForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("提交")


class RegisterForm(FlaskForm):
    name = StringField("用户名", validators=[DataRequired()])
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


@user_bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user_name = form.name.data
        password = form.password.data
        res_list = User.query.filter_by(username=user_name).all()
        for user in res_list:
            if check_password_hash(user.password, password):
                response = redirect(url_for('index.index', page=1))
                response.set_cookie('uid', str(user.id), max_age=60*60*24)
                return response
        else:
            return render_template("user/login.html", form=form, msg="用户名或密码错误，请重新输入")

    return render_template("user/login.html", form=form, msg=None)


@user_bp.route("/logout")
def logout():
    response = redirect(url_for('index.index'))
    response.delete_cookie('uid')
    return response
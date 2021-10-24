import hashlib

from flask import Blueprint, render_template, request, redirect, url_for

from flask_wtf import Form
from wtforms import TextField,StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired,DataRequired, Email, EqualTo

from apps.user.model import User
from dao import db

user_bp = Blueprint('user', __name__)


class RegisterForm(Form):
    name = StringField("名字", validators=[DataRequired()])
    email = StringField("email", validators=[Email()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo('repassword', message='Passwords must match')])
    repassword = PasswordField("再次确认密码", validators=[DataRequired()])
    accept_tos = BooleanField("我接受隐私条约", validators=[DataRequired()])
    submit = SubmitField("提交")

class LoginForm(Form):
    name = StringField("名字", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo('repassword', message='Passwords must match')])
    submit = SubmitField("提交")


@user_bp.route('/user')  # 用户主页
def user_center():
    # 查询数据库中所有用户
    user = User.query.all()
    print(user)
    return render_template('user/user_index.html',users=user)


@user_bp.route('/register', methods=['POST', 'GET'])
def user_register():
    print_name = None
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # 创建实体对象
        user = User()
        user.username = form.name.data
        user.password = hashlib.sha1(form.password.data.encode('utf-8')).hexdigest()
        user.email = form.email.data

        # 添加到数据库
        db.session.add(user)
        db.session.commit()

        print_name = user.username
        # return redirect(url_for('user.user_register'))

    return render_template("user/register.html", form=form, name=print_name)


@user_bp.route('/login',methods=['POST', 'GET'])
def user_login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        pass_input = hashlib.sha1(form.password.data.encode('utf-8')).hexdigest()
        res_list = User.query.filter_by(username=form.name.data)
        for u in res_list:
            if u.password == pass_input:
                return '用户登陆成功！'
        else:
            return render_template('user/login.html', form=form, msg="用户名或密码错误")

    return render_template('user/login.html',form=form)

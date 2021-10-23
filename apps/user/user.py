from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/') # 用户主页
def user_center():
    return '用户中心'

@user_bp.route('/register') 
def user_cregister():
    return '注册'

@user_bp.route('/login') 
def user_login():
    return '登陆'
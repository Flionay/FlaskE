from flask import Blueprint, render_template, request

from apps.user.model import User

index_bp = Blueprint('index', __name__)


@index_bp.route("/welcome")
def welcome():
    return render_template("welcome.html")


@index_bp.route('/')
def index():
    uid = request.cookies.get('uid', None)
    if uid:
        user = User.query.get(uid)
        return render_template('index.html', user=user)
    else:
        return render_template("index.html")
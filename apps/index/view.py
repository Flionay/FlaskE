from flask import Blueprint, render_template, request

from apps.article.model import Article
from apps.user.model import User

index_bp = Blueprint('index', __name__)


@index_bp.route("/welcome")
def welcome():
    return render_template("welcome.html")


@index_bp.route('/<int:page>', methods=['GET'])
def index(page=None):
    if not page:
        page=1
    article = Article.query.order_by(Article.pdatetime.desc()).paginate(page=page,per_page=4)

    return render_template('index.html', article=article.items, pagination=article)




@index_bp.app_template_filter('summary')
def summary(content):
    return content[:50]+'......'
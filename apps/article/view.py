from flask import Blueprint, render_template

article_bp = Blueprint('article', __name__)


@article_bp.route("/publish")
def publish_article():
    return render_template('publish.html')

#TODO
'''
开发博客markdown写作页面
'''
from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, HiddenField,  DateField, SelectField
from wtforms.validators import DataRequired, length

from apps.article.model import Article
from apps.categories.model import Categories
from apps.user.model import User
from exts import db

article_bp = Blueprint('article', __name__)



class PostForm(FlaskForm):
    title = TextField('Title', [DataRequired(), length(max=255)])
    text = TextAreaField('Body', [DataRequired()])
    categories = SelectField('Categories', coerce=int)
    user_id = DateField('user_id', [DataRequired()])
    body_html = HiddenField()

    def __init__(self):
        super(PostForm, self).__init__()
        self.categories.choices = [(c.id, c.categories) for c in Categories.query.order_by('id')]


@article_bp.route("/publish", methods=['POST', 'GET'])
def publish_article():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        article = Article()
        article.content = form.body
        article.title = form.title
        article.categories_id = form.categories.id
        article.author_id = User.query.filter_by(form.user_id).name

        db.session.add(article)
        db.session.commit()

        print(request.form.get("content"))
    print("------------")
    return render_template('article/editor.html', form=form)


# TODO
'''
新增categories按钮
'''

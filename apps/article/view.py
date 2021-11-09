from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, HiddenField, DateField, SelectField, SubmitField
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
    # user_id = DateField('user_id', [DataRequired()])
    # body_html = HiddenField()
    submit = SubmitField('提交文章')

    def __init__(self):
        super(PostForm, self).__init__()
        self.categories.choices = [(c.id, c.categories) for c in Categories.query.order_by('id')]


@article_bp.route("/publish", methods=['POST', 'GET'])
def publish_article():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        article = Article()
        article.content = request.form['markdownEditor']
        article.title = form.title
        article.categories_id = form.categories.id
        # article.author_id = User.query.filter_by(form.user_id).name

        print(article.title)
        #
        # db.session.add(article)
        # db.session.commit()

        print(request.form.get("content"))
        print("------------")
        return "保存文章成功"
    return render_template('article/editor.html', form=form)


# detail
@article_bp.route('/<int:page>/<int:id>', methods=['GET'])
def detail(page,id):
    if not page:
        page=1
    article = Article.query.order_by(Article.pdatetime.desc()).paginate(page=page,per_page=4)


# TODO
'''
新增categories按钮
'''

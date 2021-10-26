from datetime import datetime

from exts import db


class Article(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, )
    content = db.Column(db.Text, nullable=False)
    pdatetime = db.Column(db.DateTime, default=datetime.now)
    click_num = db.Column(db.Integer, default=0)
    save_num = db.Column(db.Integer, default=0)
    love_num = db.Column(db.Integer, default=0)
    # 外键 对应user id
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
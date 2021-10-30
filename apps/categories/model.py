from exts import db


class Categories(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    categories = db.Column(db.String(256), nullable=False)

    article = db.relationship('Article', backref='Categories', lazy='dynamic')
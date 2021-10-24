from dao import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __str__(self):
        return "user_table:"+self.username

# class UserInfo(db.Model):

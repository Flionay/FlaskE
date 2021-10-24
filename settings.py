class Config(object):
    ENV = 'development'
    SECRET_KEY = "ANGYIBLOG"
    DEBUG = True
    FLASK_APP = "app.py"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

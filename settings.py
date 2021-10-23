class Config(object):
    ENV = 'development'
    SECRET_KEY = "ANGYIBLOG"
    DEBUG = True
    FLASK_APP = "app.py"
    SQLALCHMY_DATABASE_URL = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
    

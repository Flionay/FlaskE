from flask import Flask,render_template
from Config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)  # 将应用实例传给构造函数
m = Moment(app)

@app.route("/")
def index():
    utc = datetime.utcnow()
    return render_template("user.html",current_time=utc)

@app.errorhandler(404)
def errorhandler(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

app.run()
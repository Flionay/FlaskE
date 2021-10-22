from flask import Flask,render_template
from Config import Config
app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    names = {
        "basketball":23,
        "mylist":[1,2,3]
    }
    return render_template("index.html",names=names)


@app.route('/base2')
def func_name():
    return render_template('base2.html')
app.run()
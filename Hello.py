from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",name="FLASK")

@app.route("/user")
def user():
    users = ["James","Kobe","Curry"]
    return render_template("user.html",users=users)
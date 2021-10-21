from flask import Flask 
app = Flask(__name__)

@app.route("/index/")
def index():
    return "hello flask"

@app.route("/<name>")
def hello(name):
    return f"hello {name}"
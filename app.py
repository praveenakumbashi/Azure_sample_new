from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! the API is working"

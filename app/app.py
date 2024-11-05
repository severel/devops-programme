import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/sum/<int:a>/<int:b>")
def calculate_sum(a, b):
    return str(a + b)

@app.route("/subtract/<int:a>/<int:b>")
def calculate_subtract(a, b):
    return str(a - b)
@app.route("/five")
def print_five():
    return "5"




if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 5000), host="0.0.0.0")

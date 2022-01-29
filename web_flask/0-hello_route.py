#!/usr/bin/python3
"""
Script that starts a Flask web application:
Routes:
    '/': display “Hello HBNB!”
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def task_0():
    """
    Function that returns and display
    “Hello HBNB!”
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

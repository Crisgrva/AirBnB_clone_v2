#!/usr/bin/python3
"""
Docstring
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """
    Docstring
    """
    states = storage.all("State")
    states = [state for state in states.values()]
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Docstring
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

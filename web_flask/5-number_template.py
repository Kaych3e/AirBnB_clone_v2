#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ defines hello page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ defines the hbnb route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def displayCtext(text):
    """ defines the displayc text replacing underscore symbols with a space """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displayPytext(text="is cool"):
    """ defines the python text, replace underscore symbols with a space """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def displayNum(n):
    """ defines the dynamic input int n """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n):
    """ displays dynamic page if n is an integer """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

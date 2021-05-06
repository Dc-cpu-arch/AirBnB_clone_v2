#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def default_route():
    """ default_route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """hbnb_route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ c_route """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ python_route """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ number_route """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n=None):
    """ number_template_route """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n=None):
    """ number_odd_or_even_route """
    if isinstance(n, int):
        if n % 2:
            oe = "odd"
        else:
            oe = "even"
        return render_template("6-number_odd_or_even.html", n=n, oe=oe)


if __name__ == "__main__":
    app.run()

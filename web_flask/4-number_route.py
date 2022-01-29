#!/usr/bin/python3
"""
    Script that starts a Flask web application
"""


from flask import Flask, escape

app = Flask(__name__)
"""
    Instance of the class Flask, this is the WSGI application
"""


@app.route("/", strict_slashes=False)
def homepage():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnbpage():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def textpage(text):
    return 'C {}'.format(escape(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>")
def textdefaultpage(text="is_cool"):
    return 'Python {}'.format(escape(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def numberpage(n):
        return "{} is a number".format(escape(n))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

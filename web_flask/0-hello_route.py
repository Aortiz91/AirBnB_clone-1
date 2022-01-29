#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask


app = Flask(__name__)

@app.route("/")
"""  main route """
def homepage(strict_slashes=False):
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(port = 5000, debug = True)

#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage(strict_slashes=False):
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(port = 5000, debug = True)

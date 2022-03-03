#!/usr/bin/env python3
"""
Module basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """ method to call the templates """
    return render_template('1-index.html')


class Config():
    """ configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

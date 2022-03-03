#!/usr/bin/env python3
"""
Module basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
""" app config """


@app.route('/')
def index():
    """ method to call the templates """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ method to set lenguage """
    return request.accept_languages.best_match(["en", "fr"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

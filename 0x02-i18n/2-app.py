#!/usr/bin/env python3
"""
Creates a get_locale function with the babel.localeselector decorator.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    gets the best match from the supported
    languages
    """
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def get_index():
    """get the home index for the babel app
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()

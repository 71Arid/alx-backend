#!/usr/bin/env python3
"""
Install the Babel Flask extension:
$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app.
Store it in a module-level variable named babel.
"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config_class = Config
babel = Babel(app)


@app.route('/')
def get_index():
    """renders the required html pages
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()

#!/usr/bin/env python3
"""0-app.py"""
from flask import Flask, render_template, g
from flask_babel import Babel, request, gettext
import logging


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """gets locale from the headers"""
    lang = request.args.get("locale")
    if lang:
        return lang
    return request.accept_languages.best_match(["en", "fr"])


def get_user(user_id):
    """0-app.py"""
    return users.get(user_id)


@app.before_request
def before_request():
    """0-app.py"""
    user_id = int(request.args.get("login_as", 0))
    user = get_user(user_id)
    g.user = user


@app.route('/')
def get_index():
    """initializes the paremeters for index.html
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    username = g.user['name'] if g.user else None
    if get_locale() == "fr":
        if username:
            welcome_msg = f'Vous êtes connecté en tant que {username}'
        else:
            welcome_msg = "Vous n'êtes pas connecté."
    if username:
        welcome_msg = f'You are logged in as {username}.'
    else:
        welcome_msg = 'You are not logged in.'
    return render_template(
        "5-index.html", home_title=home_title, home_header=home_header,
        welcome_msg=welcome_msg
    )


if __name__ == "__main__":
    app.run()

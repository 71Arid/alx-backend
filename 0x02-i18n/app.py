#!/usr/bin/env python3
"""0-app.py"""
from flask import Flask, render_template, g
from flask_babel import Babel, request, gettext, format_date
import pytz
import datetime as dt


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """0-app.py"""
    user_id = int(request.args.get("login_as", 0))
    user = get_user(user_id)
    g.user = user


@babel.localeselector
def get_locale():
    """gets locale from the headers"""
    lang = request.args.get("locale")
    if lang:
        return lang
    if g.user:
        locale = g.user["locale"]
        if locale in ["en", "fr"]:
            return locale
        else:
            return "fr"
    return request.accept_languages.best_match(["en", "fr"])


def get_user(user_id):
    """0-app.py"""
    return users.get(user_id)


def validate_timezone(timezone):
    try:
        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return None


@babel.timezoneselector
def get_timezone():
    """0-app.py"""
    tz = request.args.get("timezone")
    if tz and validate_timezone(tz):
        return tz
    if g.user and validate_timezone(g.user["timezone"]):
        return g.user["timezone"]
    return "UTC"


@app.route('/')
def get_index():
    """initializes the paremeters for index.html
    """
    locale = get_locale()
    tz = pytz.timezone(get_timezone())

    date = dt.datetime.now()
    localized_date = tz.localize(date)
    formatted_date = format_date(localized_date)

    home_title = gettext("home_title")
    home_header = gettext("home_header")
    current_time_message = gettext("current_time_is")
    current_time_message = current_time_message.format(formatted_date)

    username = g.user['name'] if g.user else None

    if locale == "fr":
        if username:
            welcome_msg = f"Vous êtes connecté en tant que {username}."
        else:
            welcome_msg = "Vous n'êtes pas connecté."
    else:
        if username:
            welcome_msg = f"You are logged in as {username}."
        else:
            welcome_msg = "You are not logged in."
    return render_template(
        "index.html", home_title=home_title, home_header=home_header,
        welcome_msg=welcome_msg, current_time=current_time_message
    )


if __name__ == "__main__":
    app.run()

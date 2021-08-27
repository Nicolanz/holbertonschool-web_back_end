#!/usr/bin/env python3
"""6-app config file"""
from flask import Flask, render_template, request, g, flash
from sys import exit
from flask_babel import Babel, gettext, _
from typing import Union
app = Flask(__name__)

app.secret_key = "hello"


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app.config.from_object(Config)
babel = Babel(app)


def get_user(login_as: Union[int, None] = None) -> Union[dict, None]:
    """Function to get a user"""
    if not login_as or login_as not in users.keys():
        return None

    return users[login_as]


@app.before_request
def before_request():
    """Before request function"""
    if "login_as" in request.args:
        u_id = request.args.get('login_as')
        try:
            u_id = int(u_id)
        except ValueError:
            exit(1)
        new_user = get_user(u_id)

        if new_user:
            g.user = new_user


@app.route('/')
def render_index():
    """Render template function"""
    try:
        user = g.user
        flash(_("You are logged in as %(username)s.", username=user['name']))
        return render_template('6-index.html')
    except AttributeError:
        flash(_("You are not logged in."))
        return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Get locale function"""
    if "locale" in request.args:
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    try:
        user = g.user
        if user['locale'] in app.config['LANGUAGES']:
            return user['locale']
    except AttributeError:
        pass

    lang = request.headers.get('locale')

    if lang in app.config['LANGUAGES']:
        return lang

    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

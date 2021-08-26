#!/usr/bin/env python3
"""3-app config file"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
app = Flask(__name__)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def render_index():
    """Render template function"""
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")

    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header
                           )


@babel.localeselector
def get_locale():
    """Get locale function"""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

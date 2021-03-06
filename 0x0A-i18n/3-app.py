#!/usr/bin/env python3
"""Module to initialize a basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
app = Flask(__name__)


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


home_title = gettext(u'home_title')
home_header = gettext(u'home_header')


@babel.localeselector
def get_locale():
    """Get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def render_index():
    """Render template function"""
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header
                           )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

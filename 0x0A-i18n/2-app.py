#!/usr/bin/env python3
"""2-app config file"""
from flask import Flask, render_template, request
from flask_babel import Babel
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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Get locale function"""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

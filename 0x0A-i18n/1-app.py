#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]


babel = Babel(
    app=app,
    default_locale=Config.LANGUAGES[0],
    default_timezone='UTC'
)


@app.route('/')
def render_index():
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

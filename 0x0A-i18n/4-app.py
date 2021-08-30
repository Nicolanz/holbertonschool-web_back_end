#!/usr/bin/env python3
"""4-app config file"""
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


home_title = gettext(u'home_title')
home_header = gettext(u'home_header')


@app.route('/')
def render_index():
    """Render template function"""
    return render_template('4-index.html',
                           home_title=home_title,
                           home_header=home_header
                           )


@babel.localeselector
def get_locale():
    """Get locale function"""
    if "locale" in request.args:
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

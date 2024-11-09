#!/usr/bin/env python3
"""Next module of flask with babel"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """configuration of the available language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best match of the languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Return rendered template"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
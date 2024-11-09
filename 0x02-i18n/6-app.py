#!/usr/bin/env python3
"""Next module of flask with babel"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """configuration of the available language"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

def get_user():
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None
    

@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Return the best match of the languages"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route("/")
def index():
    """Return rendered template"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
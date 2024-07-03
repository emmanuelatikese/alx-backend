#!/usr/bin/env python3
'''here we go'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en-US'
app.config['BABEL_SUPPORTED_LOCALES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    login_as = request.args.get("login_as")
    return users[int(login_as)] if login_as else None


@app.before_request
def before_request():
    act_user = get_user()
    g.user = act_user if act_user else None


@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user['locale'] if user['locale'] in ['en', 'fr'] else 'en'
    local_det = request.args.get('locale')
    if local_det in app.config['BABEL_SUPPORTED_LOCALES']:
        return local_det
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
@app.route("/locale=<locale>")
@app.route("/login_as=<login_as>")
def index(locale: str | None = None, login_as: str | None = None):
    '''first page start here'''
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    act_user = getattr(g, 'user', None)
    logged_in_as = gettext("You are logged in as")
    not_logged_in = gettext("You are not logged in.")
    return render_template(
        '5-index.html',
        home_header=home_header,
        home_title=home_title,
        act_user=act_user,
        logged_in_as=logged_in_as,
        not_logged_in=not_logged_in,
    )


if __name__ == '__main__':
    app.run()

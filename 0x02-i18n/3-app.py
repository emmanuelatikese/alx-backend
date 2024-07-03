#!/usr/bin/env python3
'''here we go'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    '''all about config settings'''
    BABEL_DEFAULT_LOCALE = 'en-US'
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    '''getting locale information'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''first page start here'''
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    return render_template(
        '3-index.html',
        home_header=home_header,
        home_title=home_title
        )


if __name__ == '__main__':
    app.run()

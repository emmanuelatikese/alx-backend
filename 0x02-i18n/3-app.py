#!/usr/bin/env python3
'''here we go'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''all about config settings'''
    BABEL_DEFAULT_LOCALE = 'en-US'
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    '''getting locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''first page start here'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()

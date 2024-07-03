#!/usr/bin/env python3
'''here we go'''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en-US'
app.config['BABEL_SUPPORTED_LOCALES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    '''first page start here'''
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    return render_template('3-index.html', home_header=home_header, home_title=home_title)


if __name__ == '__main__':
    app.run()

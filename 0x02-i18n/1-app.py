#!/usr/bin/env python3
'''here we go'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''all about config settings'''
    BABEL_DEFAULT_LOCALE = 'en-US'
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

@app.route('/')
def index():
    '''first page start here'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

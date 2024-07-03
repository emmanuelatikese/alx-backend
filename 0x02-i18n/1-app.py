#!/usr/bin/env python3
'''here we go'''
from flask import Flask, render_template
from flask_babel import Babel



app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en-US'
app.config['BABEL_SUPPORTED_LOCALES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'




@app.route('/')
def index():
    '''first page start here'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

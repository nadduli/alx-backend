#!/usr/bin/env python3
"""A Basic Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def get_index() -> str:
    """The index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
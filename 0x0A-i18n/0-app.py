#!/usr/bin/env python3
"""Setup a basic Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_index():
    """Function to render to 0-index"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

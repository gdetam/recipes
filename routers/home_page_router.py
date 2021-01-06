"""this file router for home page."""

from app import app

from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    """Router for home page."""
    return render_template('home.html')

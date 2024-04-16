#!/usr/bin/env python3
"""0-app.py
 Create a single / route and an index.html template that simply
 outputs “Welcome to Holberton” as page title (<title>)
 and “Hello world” as header (<h1>).
"""
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    """Renders the HTML page containing the contents.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('0-index.html')

# Run the Flask application
app.run()

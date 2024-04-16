#!/usr/bin/env python3
"""0-app.py
 Create a single / route and an index.html template that simply
 outputs “Welcome to Holberton” as page title (<title>)
 and “Hello world” as header (<h1>).
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """renders the html page containing the contents
    it does so when app.run is called
    """
    return render_template('0-index.html')


app.run()

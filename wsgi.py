# wsgi.py
import os
from flask import Flask, render_template
from dotenv import dotenv_values

application = Flask(__name__)

# Load configuration from .env
application.config.from_file(".env", load=dotenv_values)

@application.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    application.run()

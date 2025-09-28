# wsgi.py
import os
from flask import Flask
from dotenv import dotenv_values # Import dotenv_values

application = Flask(__name__)

# Load configuration from .env file
# The 'load' argument is a callable that parses the file content.
# dotenv_values() reads key-value pairs from a .env file.
application.config.from_file(".env", load=dotenv_values)

# Your other application setup (routes, etc.)
@application.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    application.run()
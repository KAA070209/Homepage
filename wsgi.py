import os
from app import app as application  
from flask import Flask, render_template
from dotenv import dotenv_values

application = Flask(__name__)

# Load configuration dari .env
application.config.from_file(".env", load=dotenv_values)

@application.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    application.run()

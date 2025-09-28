from app import app as application
from dotenv import load_dotenv
import os

# Load environment variables dari file .env
load_dotenv(".env")

# Set Flask config dari env
application.secret_key = os.getenv("SECRET_KEY")
application.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
application.config["PREFERRED_URL_SCHEME"] = os.getenv("PREFERRED_URL_SCHEME", "https")
application.config["SESSION_COOKIE_SECURE"] = os.getenv("SESSION_COOKIE_SECURE", "True") == "True"

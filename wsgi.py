from app import app as application
from dotenv import load_dotenv
import os

# load .env file
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

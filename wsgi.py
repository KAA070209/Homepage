import sys
import os

# Pastikan path benar
sys.path.insert(0, os.path.dirname(__file__))

# Import Flask application
from app import application

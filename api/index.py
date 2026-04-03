import os
import sys

# Add parent directory to path so we can import chtabot
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chtabot import app

# This is the entry point for Vercel
# The `app` object is the Flask WSGI application

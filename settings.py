import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
BACKEND_PORT = int(os.getenv('BACKEND_PORT'))
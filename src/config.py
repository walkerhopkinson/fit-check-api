import os
from dotenv import load_dotenv

load_dotenv()
PATH_TO_DATABASE = os.getenv("PATH_TO_DATABASE")
EBAY_API_KEY = os.getenv("EBAY_API_KEY")
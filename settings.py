from pathlib import Path  # python3 only
from dotenv import load_dotenv
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def get_token(): 
    return os.getenv("BOT_TOKEN")
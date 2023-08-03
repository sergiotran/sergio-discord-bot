import os
from dotenv import load_dotenv

load_dotenv()

def getEnv(key: str):
    res = os.environ.get(key)
    return res


import requests
from config import OLLAMA_URL,MODEL
def ask(prompt):
    r=requests.post(OLLAMA_URL,json={"model":MODEL,"prompt":prompt,"stream":False},timeout=120)
    r.raise_for_status()
    return r.json()["response"]

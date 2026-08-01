import requests
from config import OLLAMA_URL, MODEL


def ask(prompt):

    session = requests.Session()
    session.trust_env = False

    response = session.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    response.raise_for_status()

    return response.json()["response"]
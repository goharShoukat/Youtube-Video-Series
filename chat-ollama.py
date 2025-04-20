import requests

URL = "http://localhost:11434/api/generate"
response = requests.post(
    URL,
    json={
        "model": "llama3",
        "prompt": "Tell me about Tom Cruise's latest movie?",
        "stream": False,
    },
)
print(response.json()["response"])

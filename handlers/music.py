import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

def generate_music(prompt):
    url = "https://api-inference.huggingface.co/models/facebook/musicgen"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        return response.content
    else:
        return None

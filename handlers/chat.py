import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

def chat_with_ai(prompt):
    url = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}
    response = requests.post(url, headers=headers, json=payload)
    if response.ok and response.json() and isinstance(response.json(), list):
        return response.json()[0]['generated_text']
    else:
        return "Ошибка генерации ответа."

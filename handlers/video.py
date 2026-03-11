import requests
import os

REPLICATE_TOKEN = os.getenv("REPLICATE_TOKEN")

def generate_video(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {"Authorization": f"Token {REPLICATE_TOKEN}"}
    payload = {
        "version": "replicate:dream-video",
        "input": {"prompt": prompt}
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.ok and response.json().get('output_video_url'):
        return response.json().get('output_video_url')
    else:
        return "Ошибка генерации видео."

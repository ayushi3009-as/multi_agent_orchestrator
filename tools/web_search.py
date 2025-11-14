import requests
import os

API_KEY = os.getenv("SERPER_API_KEY")

def google_search(query):
    url = "https://google.serper.dev/search"
    data = {"q": query}
    headers = {"X-API-KEY": API_KEY}

    response = requests.post(url, json=data, headers=headers)
    return response.json().get("organic", [])

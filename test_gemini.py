import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('GOOGLE_API_KEY')
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url)
models = response.json()
print([m['name'] for m in models.get('models', []) if 'gemini' in m['name']])

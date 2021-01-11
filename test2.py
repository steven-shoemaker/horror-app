import requests
import json
API_URL = "https://api-inference.huggingface.co/models/stevenshoemaker/horror"
payload = json.dumps("The lonely ghost is")
headers = {"Content-Type": "application/json", "Authorization": "Bearer <YOUR_API_KEY>"}
response = requests.post(API_URL, payload, headers=headers)
print(response.json())
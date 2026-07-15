import requests
import json

res = requests.get("https://open-bible-api.vercel.app/1JN/1/1")
response = json.loads(res.text)
print(response["verse"])

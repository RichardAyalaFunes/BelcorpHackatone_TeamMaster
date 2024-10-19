import requests

payload = {
    "model": "llama3:latest",
    "message": [{"role": "user", "content": "Hello"}],
    "format": "json",
    "stream": False,  # True
    "options": {"temperature": 0.7},
}
response = requests.post("http://localhost:11434/api/chat", json=payload)
print(response.text)
# print(response.json())

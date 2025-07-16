import requests

def chat_with_ollama(prompt, model='gemma3:1b'):
  url = "http://localhost:11434/api/generate"
  payload = {
    "model": model,
    "prompt": prompt,
    "stream": False
  }
  
  response = requests.post(url, json=payload)
  response.raise_for_status()
  data = response.json()
  return data['response']

if __name__ == "__main__":
  prompt = "How can I wash my car?"
  reply = chat_with_ollama(prompt)
  print("Response: \n", reply)

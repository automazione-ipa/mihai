import requests

key = "Bearer "
headers = {"Authorization": key, "Content-Type":"application/json"}


url = "https://api.openai.com/v1/chat/completions"

prompt_type = input("quale pattern di prompt vuoi usare?")
domanda  = input("In cosa posso aiutarti?")

data = {
"model": "gpt-4o-mini",
"messages": [
    {"role": "system", "content": "Sei un espero di prompt engineering"},
    {"role": "user", "content": f"il metodo che devi usare è il prompt_type. ${domanda}. E farmi vedere gli esempi ${prompt_type} che fai (se esiste)"}
]
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])


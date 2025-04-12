import requests

key = "Bearer " 

# IMPOSTAZIONE DELL'ENDPOINT
url = "https://api.openai.com/v1/chat/completions"
# IMPOSTAZIONE DELL'HEADER con API KEY
headers = {"Authorization": key, "Content-Type":
"application/json"}

# IMPOSTAZIONE DEL BODY DELLA RICHIESTA
data = {
"model": "gpt-4o-mini",
"messages": [
    {"role": "system", "content": "Sei un professore di programmazione"},
    {"role": "user", "content": "fammi breve introduzione alle API REST. in 400 char"}
]
}

# CHIAMATA EFFETTIVA
response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])


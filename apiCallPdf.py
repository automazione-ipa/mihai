
import requests
from PyPDF2 import PdfReader

# Leggo il documento pdf
reader = PdfReader("tiramisuRicetta.pdf")

testoPdf = ''

# stampo ogni pagina
for page in reader.pages:
    testoPdf = page.extract_text()
    #print(page.extract_text())

#print(testoPdf)

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
    {"role": "system", "content": testoPdf},
    {"role": "user", "content": "per la ricetta quante uova ci vogliono?"}
]
}

# CHIAMATA EFFETTIVA
response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])


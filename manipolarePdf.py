
from PyPDF2 import PdfReader
'''
reader = PdfReader("tiramisuRicetta.pdf")
for page in reader.pages:
 print(page.extract_text())
'''

def cerca_parola(file, parola):
    reader = PdfReader(file)
    parola = parola.lower()
    
    for page in reader.pages:
        testo =  page.extract_text().lower()

        if parola in testo:
            a_capo = '\n'
            punto = '.'
            posizione_partenza = testo.find(parola) + len(parola)
            testo_successivo = testo[posizione_partenza:]
            risultato2 = ""

            for char in testo_successivo:
                if char == a_capo or char == punto:
                    break  
                risultato2 += char  
            
            print(f'"{parola}"{risultato2}')

        else:
            print(f"{parola} non è contenuta nel testo")
        #print(page.extract_text())
   

cerca_parola("tiramisuRicetta.pdf", "uova")


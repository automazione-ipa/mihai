
"""
# DA CELSIUS A FAHRENHEIT
def calcola_fahrenheit(celsius):
    gradi_fahrenheit = (celsius * 9 / 5) + 32
    return gradi_fahrenheit

gradi_celsius = float(input("inserisci i gradi: "))

gradi_far = calcola_fahrenheit(gradi_celsius)
print(f"{gradi_celsius} gradiCelsius equivalgono a : {gradi_far} gradi Fahrenehieit")

"""


"""
# FIBONACCI
i = 0
y = 1 
print( y, end="-")

for f in range(9):
    x = i + y
    print(x, end="-")
    i = y
    y = x
"""


# Creare un agente percettivo che risponde fornendo la ricetta giusta (se la conosce) per cocktail

def fornisci_ricetta(cocktail):
    cocktail = cocktail.lower()  # Normalizza l'input
      
    match cocktail:
        case "mojito":
            print("rum bianco, menta, succo di lime, zucchero di canna e soda")
        case "irish coffee":
            print("caffè bollente zuccherato corretto con whisky irlandese e ricoperto in superficie da uno strato di panna liquida leggermente montata")
        case "margarita":
            print("triple sec, succo di lime e tequila")
        case _:
            print("non conosco la ricetta, mi dispiace")
    
cocktail_richiesto  = input("che cocktail vuoi preparare? ")

fornisci_ricetta(cocktail_richiesto)
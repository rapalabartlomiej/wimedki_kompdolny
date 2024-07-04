import json

symbole = [
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
    "C11", "C12", "C13", "C13a", "C14", "C15", "C16", "C16a", "C17", "C18", "C19"
]

slownik = {}

for symbol in symbole:
    if symbol == "C17":
        slownik[symbol] = {'ksztalt': 'PROSTOKAT', 'kolor': 'Z CZARNYM'}
    elif symbol in ["C18", "C19"]:
        slownik[symbol] = {'ksztalt': 'KOLO', 'kolor': 'Z CZARNYM'}
    else:
        slownik[symbol] = {'ksztalt': 'KOLO', 'kolor': 'BEZ CZARNEGO'}

# Zapisanie słownika do pliku JSON
with open('symbole.json', 'w') as json_file:
    json.dump(slownik, json_file, indent=4)

print("Plik JSON został utworzony pomyślnie.")

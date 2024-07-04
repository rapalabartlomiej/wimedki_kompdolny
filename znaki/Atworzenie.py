import json

# Utworzenie słownika zgodnie z wymaganiami
slownik = {}
symbole_A = [
    "A1", "A2", "A3", "A4", "A5", "A6a", "A6b", "A6c", "A6d", "A6e",
    "A7", "A8", "A9", "A10", "A11", "A11a", "A12a", "A12b", "A12c", "A13",
    "A14", "A15", "A16", "A17", "A18a", "A18b", "A19", "A20", "A21", "A22",
    "A23", "A24", "A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33", "A34"
]
for i in range(len(symbole_A)):
    if symbole_A[i] == "A7":
        slownik[symbole_A[i]] = {'ksztalt': 'TROJKAT', 'kolor': 'BEZ CZARNEGO'}
    else:
        slownik[symbole_A[i]] = {'ksztalt': 'TROJKAT', 'kolor': 'Z CZARNYM'}

# Zapisanie słownika do pliku JSON
with open('slownik.json', 'w') as json_file:
    json.dump(slownik, json_file, indent=4)

print("Plik JSON został utworzony pomyślnie.")
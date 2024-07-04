import json

znaki = [
    "B1", "B2", "B3", "B3a", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
    "B11", "B12", "B13", "B13a", "B14", "B15", "B16", "B17", "B18", "B19",
    "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27", "B28", "B29",
    "B30", "B31", "B32", "B33", "B34", "B35", "B36", "B37", "B38", "B39",
    "B40", "B41", "B42", "B43", "B44"
]

slownik = {}

for znak in znaki:
    if znak in ["B1", "B2", "B35", "B36", "B37", "B38"]:
        slownik[znak] = {'ksztalt': 'KOLO', 'kolor': 'BEZ CZARNEGO'}        
    elif znak in ["B44", "B43", "B40", "B39"]:
        slownik[znak] = {'ksztalt': 'KWADRAT','kolor': 'Z CZARNYM'}        
    elif znak == "B20":
        slownik[znak] = {'ksztalt': 'B20', 'kolor': 'BEZ CZARNEGO'}        
    else:
        slownik[znak] = {'ksztalt': 'KOLO', 'kolor': 'Z CZARNYM'}

# Zapisanie słownika do pliku JSON
with open('znaki.json', 'w') as json_file:
    json.dump(slownik, json_file, indent=4)

print("Plik JSON został utworzony pomyślnie.")

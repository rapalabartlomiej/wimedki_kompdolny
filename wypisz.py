import os
import glob
import csv
import re
import wasisdas
import time

def najnowszy_plik_csv(sciezka_folderu):
    lista_plikow = glob.glob(os.path.join(sciezka_folderu, '*.csv'))
    if not lista_plikow:
        return None
    return max(lista_plikow, key=os.path.getctime)

sciezka_folderu = r"F:\pobrane"  # Użyj r przed ścieżką, aby interpretować ją dosłownie (bez escape'owania)
najnowszy_plik = najnowszy_plik_csv(sciezka_folderu)

pattern = r"\"(?:ZNAK|TABLICA\/U\/3\/[AB]|TABLICZKA).*\/[0-9x]*\/(?:OCO|AL)\/(?:1,25|1,5)\/(?:NM|M)\/K\/(?:F|0)\/(?:1|2|3)"
tablica = []
if najnowszy_plik:
    print("Najnowszy plik CSV:", najnowszy_plik)
    print("Zawartość pliku:")
    
    with open(najnowszy_plik, 'r', newline='') as plik_csv:
        reader = csv.DictReader(plik_csv, delimiter=';')
        for row in reader:
            #if re.match(r'^ZKS.*2024$', row["Zamowienie"]) :  # Używamy wyrażenia regularnego do sprawdzenia początku wartości w pierwszej kolumnie
            tablica.append(row)
else:
    print("Brak plików CSV w folderze", sciezka_folderu)
print(pattern)
ar = []
for row in tablica:
    if re.search(r"(?:ZNAK\/|TABLICA\/U\/3\/[AB]|TABLICZKA).*\/[0-9x]*\/(?:OCO|AL)\/(?:1,25|1,5)\/(?:NM|M)\/K\/(?:F|0)\/(?:1|2|3).*",row["Pa Id"]):
        ar.append(row["Pa Id"])
        #print("przyjmuje:" + row["Pa Id"])
    else:
        print("odrzucam:" + row["Pa Id"])
    time.sleep(0.1)
        
for i in ar:
    print(wasisdas.interpretacjaKodu(i))
    time.sleep(0.05)
    

    

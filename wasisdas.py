import re
print(re.search(r"(?:ZNAK|TABLICA\/U\/3\/[AB]|TABLICZKA).*\/[0-9x]*\/(?:OCO|AL)\/(?:1,25|1,5)\/(?:NM|M)\/K\/(?:F|0)\/(?:1|2|3).*","ZNAK/G/1/F/300x1000/OCO/1,25/M/K/F/2"))

def wynikaniezinformacji(tablica):
    #ma sie dowiedziec o nazwa czarnym,ksztalcie,i certyfikat 

    nazwa = tablica[0]
    rozmiar = tablica[1]
    malowany = tablica[2]
    
    if malowany == "NM":
        return [nazwacamel(nazwa),"-","-","nie"]
    
    return [nazwacamel(nazwa),rozmiar,"chuj wie","tak"]
    
def nazwacamel(napis):
    if napis == "T TRESC":
        return napis
    return napis.replace(" ", "").capitalize()

def interpretacjaKodu(napis):
    podzielony_string = napis.split('/')
    
    folia = podzielony_string[-1]
    podzielony_string.pop() 
    
    profil = podzielony_string[-1]
    podzielony_string.pop() 
    
    klejony = podzielony_string[-1]
    podzielony_string.pop() 
    
    malowany = podzielony_string[-1]
    podzielony_string.pop() 
    
    grubosc = podzielony_string[-1]
    podzielony_string.pop() 
    
    material = podzielony_string[-1]
    podzielony_string.pop() 
    
    rozmiar = podzielony_string[-1]
    podzielony_string.pop() 
    
    nazwa = ""
    for i in range(1,len(podzielony_string)):
        nazwa = nazwa + " " + podzielony_string[i]
    
    print("........"+str(wynikaniezinformacji([nazwa,rozmiar,malowany])[0]))
    #return [nazwa,rozmiar,malowany]
    return 1
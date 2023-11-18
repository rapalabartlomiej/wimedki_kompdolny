import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pyperclip

def wybierz_zks():
    zks_button.config(bg="red")
    zkp_button.config(bg="white")
    inne_button.config(bg="white")
    zks_button_var.set(True)
    zkp_button_var.set(False)
    inne_button_var.set(False)
    tekst_entry_inne.config(state=tk.DISABLED)

def wybierz_zkp():
    zkp_button.config(bg="red")
    zks_button.config(bg="white")
    inne_button.config(bg="white")
    zkp_button_var.set(True)
    zks_button_var.set(False)
    inne_button_var.set(False)
    tekst_entry_inne.config(state=tk.DISABLED)

def wybierz_inne():
    inne_button.config(bg="red")
    zks_button.config(bg="white")
    zkp_button.config(bg="white")
    inne_button_var.set(True)
    zks_button_var.set(False)
    zkp_button_var.set(False)
    tekst_entry_inne.config(state=tk.NORMAL)

def wybierz_folia1():
    folia1_button.config(bg="red")
    folia2_button.config(bg="white")
    folia3_button.config(bg="white")
    folia1_button_var.set(True)
    folia2_button_var.set(False)
    folia3_button_var.set(False)

def wybierz_folia2():
    folia2_button.config(bg="red")
    folia1_button.config(bg="white")
    folia3_button.config(bg="white")
    folia2_button_var.set(True)
    folia1_button_var.set(False)
    folia3_button_var.set(False)

def wybierz_folia3():
    folia3_button.config(bg="red")
    folia1_button.config(bg="white")
    folia2_button.config(bg="white")
    folia3_button_var.set(True)
    folia1_button_var.set(False)
    folia2_button_var.set(False)

def wybierz_ocynk():
    ocynk_button.config(bg="red")
    aluminum_button.config(bg="white")
    ocynk_button_var.set(True)
    aluminum_button_var.set(False)
    profil_button_var.set(False)
    bez_profilu_button_var.set(False)

def wybierz_aluminum():
    aluminum_button.config(bg="red")
    ocynk_button.config(bg="white")
    aluminum_button_var.set(True)
    ocynk_button_var.set(False)
    profil_button_var.set(False)
    bez_profilu_button_var.set(False)

def wybierz_profil():
    profil_button.config(bg="red")
    bez_profilu_button.config(bg="white")
    profil_button_var.set(True)
    bez_profilu_button_var.set(False)

def wybierz_bez_profilu():
    bez_profilu_button.config(bg="red")
    profil_button.config(bg="white")
    bez_profilu_button_var.set(True)
    profil_button_var.set(False)

def wybierz_kwadrat():
    kwadrat_button.config(bg="red")
    prostokat_button.config(bg="white")
    trojkat_button.config(bg="white")
    romb_button.config(bg="white")
    osmiokat_button.config(bg="white")
    kolo_button.config(bg="white")
    kwadrat_button_var.set(True)
    prostokat_button_var.set(False)
    trojkat_button_var.set(False)
    romb_button_var.set(False)
    osmiokat_button_var.set(False)

def wybierz_prostokat():
    prostokat_button.config(bg="red")
    kwadrat_button.config(bg="white")
    trojkat_button.config(bg="white")
    romb_button.config(bg="white")
    osmiokat_button.config(bg="white")
    kolo_button.config(bg="white")
    prostokat_button_var.set(True)
    kwadrat_button_var.set(False)
    trojkat_button_var.set(False)
    romb_button_var.set(False)
    osmiokat_button_var.set(False)
    kolo_button_var.set(False)

def wybierz_trojkat():
    trojkat_button.config(bg="red")
    kwadrat_button.config(bg="white")
    prostokat_button.config(bg="white")
    romb_button.config(bg="white")
    osmiokat_button.config(bg="white")
    kolo_button.config(bg="white")
    trojkat_button_var.set(True)
    kwadrat_button_var.set(False)
    prostokat_button_var.set(False)
    romb_button_var.set(False)
    osmiokat_button_var.set(False)
    kolo_button_var.set(False)

def wybierz_romb():
    romb_button.config(bg="red")
    kwadrat_button.config(bg="white")
    prostokat_button.config(bg="white")
    trojkat_button.config(bg="white")
    osmiokat_button.config(bg="white")
    kolo_button.config(bg="white")
    romb_button_var.set(True)
    kwadrat_button_var.set(False)
    prostokat_button_var.set(False)
    trojkat_button_var.set(False)
    osmiokat_button_var.set(False)
    kolo_button_var.set(False)

def wybierz_osmiokat():
    osmiokat_button.config(bg="red")
    kwadrat_button.config(bg="white")
    prostokat_button.config(bg="white")
    trojkat_button.config(bg="white")
    romb_button.config(bg="white")
    kolo_button.config(bg="white")
    osmiokat_button_var.set(True)
    kwadrat_button_var.set(False)
    prostokat_button_var.set(False)
    trojkat_button_var.set(False)
    romb_button_var.set(False)
    kolo_button_var.set(False)

def wybierz_kolo():
    osmiokat_button.config(bg="white")
    kolo_button.config(bg="red")
    kwadrat_button.config(bg="white")
    prostokat_button.config(bg="white")
    trojkat_button.config(bg="white")
    romb_button.config(bg="white")
    osmiokat_button_var.set(False)
    kwadrat_button_var.set(False)
    prostokat_button_var.set(False)
    trojkat_button_var.set(False)
    romb_button_var.set(False)
    kolo_button_var.set(True)

def wybierz_z_czarnym():
    czarny_button.config(bg="red")
    bez_czarnego_button.config(bg="white")
    czarny_button_var.set(True)
    bez_czarnego_button_var.set(False)

def wybierz_bez_czarnego():
    bez_czarnego_button.config(bg="red")
    czarny_button.config(bg="white")
    bez_czarnego_button_var.set(True)
    czarny_button_var.set(False)

def wybierz_125():
    przycisk_125.config(bg="red")
    przycisk_150.config(bg="white")
    przycisk_125_var.set(True)
    przycisk_150_var.set(False)
    
def wybierz_150():
    przycisk_150.config(bg="red")
    przycisk_125.config(bg="white")
    przycisk_150_var.set(True)
    przycisk_125_var.set(False)
    
def lokalizacja(folia,rodzaj,profil,ksztalt,kolor):
    if ksztalt == "B20" or ksztalt == "ROMB":
        kolor = "Z CZARNYM"    
    
    lokalizacja = fr"C:\Users\hala\Desktop\ZNAKI ETYKIETY 2021 FOLIA TYP {str(folia)} ORALITE"
    if rodzaj == "oc":
        lokalizacja = f"{lokalizacja}/OCYNK"
    elif rodzaj == "al":
        lokalizacja = f"{lokalizacja}/ALUMINIUM"
    
    if kolor == "Z CZARNYM":
        lokalizacja = f"{lokalizacja}/{ksztalt} {profil}"
    if kolor == "BEZ CZARNEGO" and ksztalt != "TRÓJKĄT":
        lokalizacja = f"{lokalizacja}/{ksztalt} {profil} -- {ksztalt} {kolor}"
    if kolor == "BEZ CZARNEGO" and ksztalt == "TRÓJKĄT":
        lokalizacja = f"{lokalizacja}/{ksztalt} {profil} -- ZNAK A7 {kolor}"  
  
    return lokalizacja





array=[[]]
def dodajDoTabeli(): 
    # jaki numer zamowienia
    nr_zamowienia = ""
    if zks_button_var.get():
        nr_zamowienia = "ZKS"
    elif zkp_button_var.get():
        nr_zamowienia = "ZKP"
    elif inne_button_var.get():
        nr_zamowienia = tekst_entry_inne.get()        
    user_input_koncowka = tekst_entry_koncowka.get()
    final_text = user_input_koncowka
    if len(final_text) < 6 and len(final_text) != 0:
        while len(final_text) != 6:
            final_text = "0" + final_text
    nr_zamowienia = f"{nr_zamowienia}/{final_text}/2023"
    print(nr_zamowienia)
    #jaka folia
    folia = 0
    if folia1_button_var.get():
        folia = 1
    elif folia2_button_var.get():
        folia = 2
    elif folia3_button_var.get():
        folia = 3
    #rodzaj
    rodzaj = ""
    if ocynk_button_var.get():
        rodzaj = "oc"
    elif aluminum_button_var.get():
        rodzaj = "al"
    #kolor
    kolor = ""
    if czarny_button_var.get():
        kolor = "Z CZARNYM"
    elif bez_czarnego_button_var.get():
        kolor = "BEZ CZARNEGO"
    #profil
    profil = ""
    if profil_button_var.get():
        profil = f"Z PROFILEM"
    elif bez_profilu_button_var.get():
        profil = f"BEZ PROFILA"
    #ksztalt
    ksztalt = ""
    if kwadrat_button_var.get():
        ksztalt = "KWADRAT"
    elif prostokat_button_var.get():
        ksztalt = "PROSTOKĄT"
    elif trojkat_button_var.get():
        ksztalt = "TRÓJKĄT"
    elif romb_button_var.get():
        ksztalt = "ROMB"
    elif osmiokat_button_var.get():
        ksztalt = "B20"
    elif kolo_button_var.get():
        ksztalt = "KOŁO"
    ###############
        
    if tekst_size.get():
        rozmiar = f"{tekst_size.get()}"

    if tekst_symbol.get():
        symbol = f"{tekst_symbol.get()}"

    grubosc = ""
    if przycisk_125_var.get():
        grubosc = "1.25"
    elif przycisk_150_var.get():
        grubosc = "1.5"

    #print(lokalizacja(folia,rodzaj,profil,ksztalt,kolor))
    # Dodanie danych do tabeli
    tree.insert("", "end", text="",values=(nr_zamowienia, folia,  rodzaj,  profil  ,ksztalt,kolor,  symbol,rozmiar,grubosc))
    
    

# Tworzenie głównego okna
root = tk.Tk()
root.title("Linia z przyciskami")

# Zmienna do przechowywania stanu przycisków ZKS, ZKP i Inne
zks_button_var = tk.BooleanVar()
zkp_button_var = tk.BooleanVar()
inne_button_var = tk.BooleanVar()

# Zmienna do przechowywania stanu przycisków wyboru folii
folia1_button_var = tk.BooleanVar()
folia2_button_var = tk.BooleanVar()
folia3_button_var = tk.BooleanVar()

# Zmienna do przechowywania stanu przycisków Ocynk, Aluminum, Profil i Bez Profilu
ocynk_button_var = tk.BooleanVar()
aluminum_button_var = tk.BooleanVar()
profil_button_var = tk.BooleanVar()
bez_profilu_button_var = tk.BooleanVar()

# Zmienna do przechowywania stanu przycisków wyboru figur geometrycznych
kwadrat_button_var = tk.BooleanVar()
prostokat_button_var = tk.BooleanVar()
trojkat_button_var = tk.BooleanVar()
romb_button_var = tk.BooleanVar()
osmiokat_button_var = tk.BooleanVar()
kolo_button_var = tk.BooleanVar()

# Zmienna do przechowywania stanu przycisków wyboru "z czarnym" i "bez czarnego"
czarny_button_var = tk.BooleanVar()
bez_czarnego_button_var = tk.BooleanVar()

# Zmienna do przechowywania stanu przycisków wyboru "1.25" i "1.5"
przycisk_125_var = tk.BooleanVar()
przycisk_150_var = tk.BooleanVar()

# Zmienna do przechowywania stanu przycisków wyboru blacha, ksztalt, kolor
blacha_var = tk.StringVar()
profil_var = tk.StringVar()
ksztalt_var = tk.StringVar()
kolor_var = tk.StringVar()

# Przyciski ZKS, ZKP i Inne
zks_button = tk.Button(root, text="ZKS", relief=tk.RAISED, command=wybierz_zks, highlightthickness=0)
zkp_button = tk.Button(root, text="ZKP", relief=tk.RAISED, command=wybierz_zkp, highlightthickness=0)
inne_button = tk.Button(root, text="Inne", relief=tk.RAISED, command=wybierz_inne, highlightthickness=0)

# Pole tekstowe dla przycisku "Inne"
tekst_entry_inne = tk.Entry(root, width=5, state=tk.DISABLED)  # Ograniczenie pola tekstowego do pięciu liter

# Pole tekstowe dla końcówki tekstu
tekst_entry_koncowka = tk.Entry(root, width=10)

# Przyciski wyboru folii
folia1_button = tk.Button(root, text="Folia 1", relief=tk.RAISED, command=wybierz_folia1, highlightthickness=0)
folia2_button = tk.Button(root, text="Folia 2", relief=tk.RAISED, command=wybierz_folia2, highlightthickness=0)
folia3_button = tk.Button(root, text="Folia 3", relief=tk.RAISED, command=wybierz_folia3, highlightthickness=0)

# Przyciski wyboru Ocynk i Aluminum
ocynk_button = tk.Button(root, text="Ocynk", relief=tk.RAISED, command=wybierz_ocynk, highlightthickness=0)
aluminum_button = tk.Button(root, text="Aluminum", relief=tk.RAISED, command=wybierz_aluminum, highlightthickness=0)

# Przyciski wyboru Profil i Bez Profilu
profil_button = tk.Button(root, text="Profil", relief=tk.RAISED, command=wybierz_profil, highlightthickness=0)
bez_profilu_button = tk.Button(root, text="Bez profila", relief=tk.RAISED, command=wybierz_bez_profilu, highlightthickness=0)

# Przyciski wyboru figur geometrycznych
kwadrat_button = tk.Button(root, text="Kwadrat", relief=tk.RAISED, command=wybierz_kwadrat, highlightthickness=0)
prostokat_button = tk.Button(root, text="Prostokąt", relief=tk.RAISED, command=wybierz_prostokat, highlightthickness=0)
trojkat_button = tk.Button(root, text="Trójkąt", relief=tk.RAISED, command=wybierz_trojkat, highlightthickness=0)
romb_button = tk.Button(root, text="Romb", relief=tk.RAISED, command=wybierz_romb, highlightthickness=0)
osmiokat_button = tk.Button(root, text="Ośmiokąt", relief=tk.RAISED, command=wybierz_osmiokat, highlightthickness=0)
kolo_button = tk.Button(root, text="Kolo", relief=tk.RAISED, command=wybierz_kolo, highlightthickness=0)

# Przyciski wyboru "z czarnym" i "bez czarnego"
czarny_button = tk.Button(root, text="Z czarnym", relief=tk.RAISED, command=wybierz_z_czarnym, highlightthickness=0)
bez_czarnego_button = tk.Button(root, text="Bez czarnego", relief=tk.RAISED, command=wybierz_bez_czarnego, highlightthickness=0)

# Przyciski wyboru "1.25" i "1.5"
przycisk_125 = tk.Button(root, text="1.25", relief=tk.RAISED, command=wybierz_125, highlightthickness=0)
przycisk_150 = tk.Button(root, text="1.5", relief=tk.RAISED, command=wybierz_150, highlightthickness=0)

# Przycisk "Dodaj"
dodaj_button = tk.Button(root, text="Dodaj", command=dodajDoTabeli)

# pole tekstowe oznaczenie znaka
symbol = tk.Label(root, text="SYMBOL:")
symbol.grid(row=6, column=0, padx=5, pady=5)

tekst_symbol = tk.Entry(root, width=10)
tekst_symbol.grid(row=6, column=1, padx=5, pady=5)

label = tk.Label(root, text="ROZMIAR:")
label.grid(row=6, column=2, padx=5, pady=5)

tekst_size = tk.Entry(root, width=10)
tekst_size.grid(row=6, column=3, padx=5, pady=5)

# Ustawienie odstępów między elementami
zks_button.grid(row=0, column=0, padx=5, pady=5)
zkp_button.grid(row=0, column=1, padx=5, pady=5)
inne_button.grid(row=0, column=2, padx=5, pady=5)
tekst_entry_inne.grid(row=0, column=3, padx=5, pady=5)
tekst_entry_koncowka.grid(row=0, column=4, padx=5, pady=5)

ocynk_button.grid(row=2, column=1, padx=5, pady=5,)
aluminum_button.grid(row=2, column=0, padx=5, pady=5,)
przycisk_125.grid(row=2, column=2, padx=5, pady=5)
przycisk_150.grid(row=2, column=3, padx=5, pady=5)

profil_button.grid(row=3, column=0, padx=5, pady=5)
bez_profilu_button.grid(row=3, column=1, padx=5, pady=5)

czarny_button.grid(row=3, column=2, padx=5, pady=5,)
bez_czarnego_button.grid(row=3, column=3, padx=5, pady=5,)

folia1_button.grid(row=1, column=0, padx=5, pady=5)
folia2_button.grid(row=1, column=1, padx=5, pady=5)
folia3_button.grid(row=1, column=2, padx=5, pady=5)

kwadrat_button.grid(row=4, column=0, padx=5, pady=5)
prostokat_button.grid(row=4, column=1, padx=5, pady=5)
trojkat_button.grid(row=4, column=2, padx=5, pady=5)
romb_button.grid(row=4, column=3, padx=5, pady=5)
osmiokat_button.grid(row=4, column=4, padx=5, pady=5)
kolo_button.grid(row=4, column=5, padx=5, pady=5)




dodaj_button.grid(row=8, column=0, columnspan=5, padx=5, pady=10)  # Button ma columnspan=5, aby rozciągnąć się przez cały rzęd





# Przycisk "Usuń"
def usun_zaznaczone():
    selected_items = tree.selection()
    for item in selected_items:
        tree.delete(item)
usun_button = tk.Button(root, text="Usuń", command=usun_zaznaczone)
usun_button.grid(row=8, column=6, padx=5, pady=10)










def pobierz_dane_z_drzewa(tree):
    dane = []
    for item_id in tree.get_children():
        # Pobieranie wartości dla danego elementu
        values = tree.item(item_id, "values")
        
        # Dodawanie wartości do tablicy
        dane.append(values)
    
    return dane

def print_dane():
    dane = pobierz_dane_z_drzewa(tree)
    print(type(dane))
    print("Dane z drzewa:")
    for row in dane:
        print(row[0])


button_pobierz_dane = tk.Button(root, text="Pobierz dane", command=print_dane)
button_pobierz_dane.grid(row=9, column=6, padx=5, pady=10)















# Tabela po prawej stronie
tree = ttk.Treeview(root, columns=("Button", "Text", "Blacha", "Profil", "Kształt", "Kolor", "Symbol", "Rozmiar", "1.25/1.5"))
# Ustaw szerokość kolumny numer 1 na 20 pikseli
for col in ("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"):
    tree.column(col, width=80)

tree.heading("#0", text="ID")
tree.heading("#1", text="NR_ZAMÓWIENIA")
tree.heading("#2", text="FOLIA")
tree.heading("#3", text="ROZMIAR")
tree.heading("#4", text="PROFIL")
tree.heading("#5", text="KSZTAŁT")
tree.heading("#6", text="KOLOR")
tree.heading("#7", text="SYMBOL")
tree.heading("#8", text="RODZAJ_BLACHY")
tree.heading("#9", text="GRUBOŚĆ_BLACHY")

tree.grid(row=0, column=6, rowspan=5, padx=0, pady=0)

root.mainloop()

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pyperclip
import time
import subprocess
import keyboard
import csv
import re

#region preset
def set_D18a():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "D18a")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "600x750")
    wybierz_bez_czarnego()
    wybierz_prostokat()
    pole_ilosc_wimedek.focus_set()
   
    
def set_u3a_and_size():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "U3a")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "600x600")
    wybierz_bez_czarnego()
    wybierz_kwadrat()
def set_B43():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "B43")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "600x600")
    wybierz_z_czarnym()
    wybierz_kwadrat()
def set_B44():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "B44")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "600x600")
    wybierz_z_czarnym()
    wybierz_kwadrat()
def set_u3a_bez_czarnego_prostokat():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "U3a")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "600x600")
    wybierz_bez_czarnego()
    wybierz_prostokat()

def set_u6a_bez_czarnego_prostokat():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "U6a")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "500x750")
    wybierz_bez_czarnego()
    wybierz_prostokat()

def set_e15_prostokat_z_czarnym():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "E15")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "600x300")
    wybierz_z_czarnym()
    wybierz_prostokat()

def set_g1_bez_czarnego_prostokat():
    pole_nazwy_znaku.delete(0, tk.END)
    pole_nazwy_znaku.insert(0, "G1")
    pole_rozmiaru_znaku.delete(0, tk.END)
    pole_rozmiaru_znaku.insert(0, "300x1000")
    wybierz_bez_czarnego()
    wybierz_prostokat()
#endregion
#region przyciski

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
    

def wybierz_aluminum():
    aluminum_button.config(bg="red")
    ocynk_button.config(bg="white")
    aluminum_button_var.set(True)
    ocynk_button_var.set(False)

def wybierz_profil():
    profil_button.config(bg="red")
    bez_profilu_button.config(bg="white")
    profil_button_var.set(True)
    bez_profilu_button_var.set(False)
    odznacz_certyfikacje()
    

def wybierz_bez_profilu():
    bez_profilu_button.config(bg="red")
    profil_button.config(bg="white")
    bez_profilu_button_var.set(True)
    profil_button_var.set(False)
    odznacz_certyfikacje()
    

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
    odznacz_certyfikacje()

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
    odznacz_certyfikacje()

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
    odznacz_certyfikacje()

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
    odznacz_certyfikacje()

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
    odznacz_certyfikacje()

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
    odznacz_certyfikacje()

def wybierz_z_czarnym():
    czarny_button.config(bg="red")
    bez_czarnego_button.config(bg="white")
    czarny_button_var.set(True)
    bez_czarnego_button_var.set(False)
    odznacz_certyfikacje()
    

def wybierz_bez_czarnego():
    bez_czarnego_button.config(bg="red")
    czarny_button.config(bg="white")
    bez_czarnego_button_var.set(True)
    czarny_button_var.set(False)
    odznacz_certyfikacje()
    
def odznacz_certyfikacje():
    bez_certyfikat_button.config(bg="white")
    bez_certyfikat_button_var.set(False)
    frame_buttons.config(bg="white")

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
    
def wybierz_bez_certyfikatu():
    frame_buttons.config(bg="black")
    bez_certyfikat_button.config(bg="red")
    bez_certyfikat_button_var.set(True)
#endregion

def funkcja_po_enter(event):
    pierwsza_litera = pole_nazwy_znaku.get()
    pierwsza_litera= pierwsza_litera[0]
    tekst = pole_nazwy_znaku.get()
    
    
    if bez_certyfikat_button_var.get() == 0:
        if pierwsza_litera=="A":
            wybierz_trojkat()
            if tekst == "A7":
                wybierz_bez_czarnego()
            else:
                wybierz_z_czarnym()
        if tekst[0] =="D":
            if tekst == "D1" or tekst == "D2":
                wybierz_romb()
                wybierz_z_czarnym()
            else:
                numer = tekst[1:]
                numer = numer.replace('a','')
                numer = numer.replace('b','')
                numer = numer.replace('c','')
                numer = numer.replace('d','')
                print(numer)
                numer = int(numer)
                if numer in {6, 15, 16, 17, *range(23, 35), 37, 38, *range(44, 48), 52, 53}:
                    wybierz_z_czarnym()
                    print("roo")
                else:
                    wybierz_bez_czarnego()

 
#region dodawanie usuwanie itd                      
def lokalizacja(folia,rodzaj,profil,ksztalt,kolor):
    if ksztalt == "B20" or ksztalt == "ROMB":
        kolor = "Z CZARNYM"    
    
    lokalizacja = f"C:\\Users\\hala\\Desktop\\ZNAKI ETYKIETY 2024 FOLIA TYP {str(folia)} ORALITE"
    if rodzaj == "oc":
        lokalizacja = f"{lokalizacja}\\OCYNK"
    elif rodzaj == "al":
        lokalizacja = f"{lokalizacja}\\ALUMINIUM"
    print("=")
    print(ksztalt)
    if kolor == "Z CZARNYM":
        lokalizacja = f"{lokalizacja}\\{ksztalt} {profil}"
    if kolor == "BEZ CZARNEGO" and ksztalt != "TRÓJKĄT":
        lokalizacja = f"{lokalizacja}\\{ksztalt} {profil} — {ksztalt} {kolor}"
    if kolor == "BEZ CZARNEGO" and ksztalt == "TRÓJKĄT":
        lokalizacja = f"{lokalizacja}\\{ksztalt} {profil} — ZNAK A7 {kolor}"  
  
    return lokalizacja

def dodajDoTabeli(): 
    # jaki numer zamowienia
    
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
    nr_zamowienia = f"{nr_zamowienia}/{final_text}/2024"
    print(nr_zamowienia)
    #jaka folia
    
    if folia1_button_var.get():
        folia = 1
    elif folia2_button_var.get():
        folia = 2
    elif folia3_button_var.get():
        folia = 3
    #rodzaj
    
    
    
    if ocynk_button_var.get():
        rodzaj = "oc"
    elif aluminum_button_var.get():
        rodzaj = "al"
    #kolor
    print(bez_certyfikat_button_var.get())
    if not bez_certyfikat_button_var.get():
        if czarny_button_var.get():
            kolor = "Z CZARNYM"
        elif bez_czarnego_button_var.get():
            kolor = "BEZ CZARNEGO"
        #profil        
        if profil_button_var.get():
            profil = f"Z PROFILEM"
        elif bez_profilu_button_var.get():
            profil = f"BEZ PROFILA"
        #ksztalt     
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
        certyfikat = "tak"
    else:
        ksztalt = "-"
        profil = "-"
        kolor = "-"
        certyfikat = "nie"
        
    if pole_rozmiaru_znaku.get():
        rozmiar = f"{pole_rozmiaru_znaku.get()}"

    if pole_nazwy_znaku.get():
        symbol = f"{pole_nazwy_znaku.get()}"

    
    if przycisk_125_var.get():
        grubosc = "1.25"
    elif przycisk_150_var.get():
        grubosc = "1.5"
    if pole_ilosc_wimedek.get():
        ilosc_wimedek = pole_ilosc_wimedek.get()
    else:
        ilosc_wimedek = 1

    #print(lokalizacja(folia,rodzaj,profil,ksztalt,kolor))
    # Dodanie danych do tabeli
    tree.insert("", "end", text="",values=(ilosc_wimedek,nr_zamowienia, folia, rozmiar ,  profil  ,ksztalt,kolor,  symbol,rodzaj,grubosc,certyfikat))
    
def usun_zaznaczone():
    selected_items = tree.selection()
    for item in selected_items:
        tree.delete(item)
def pobierz_dane_z_tabeli(tree):
    dane = []
    for item_id in tree.get_children():
        # Pobieranie wartości dla danego elementu
        values = tree.item(item_id, "values")
        
        # Dodawanie wartości do tablicy
        dane.append(values)
    
    return dane
def drukuj_wszystko():
    dane = pobierz_dane_z_tabeli(tree)
    print(type(dane))
    print("Dane z drzewa:")
    x = 0.07
    for row in dane:
        print(row)
        if row[10]=="tak":
            lok = lokalizacja(row[2],row[8],row[4],row[5],row[6])+".etx"
            print(lok)
        else:
            lok="niecertyfikowane" #------------- tutaj lokalizcja do niecertyfikowanych
        #call(('cmd', '/c', 'start', '"C:\\Users\\hala\\Desktop\\ZNAKI ETYKIETY 2021 FOLIA TYP 2 ORALITE\\OCYNK\\KOŁO BEZ PROFILA — KOŁO BEZ CZARNEGO.etx"'))

        file_path = lok
        print("drukuje ========" + lok)

        try:
            process = subprocess.Popen(['cmd', '/c', 'start', '', file_path], shell=True, stderr=subprocess.DEVNULL)
            exit_code = process.wait() 
            if exit_code != 0:
                raise Exception("Proces zakończył się błędem.")
            print("----------------")
        except Exception as e:
            print("Nie udało się uruchomić procesu:", e)
            subprocess.call(('taskkill', '/F', '/IM', 'etiLABEL.exe'))
        else:  
            print("drukuje")
            keyboard.press_and_release('ctrl+p')
            time.sleep(x)
            keyboard.press_and_release('ctrl+a')
            time.sleep(x)
            pyperclip.copy(row[1])
            time.sleep(x)
            keyboard.press_and_release('ctrl+v')
            time.sleep(x)
            keyboard.press_and_release('tab')
            time.sleep(x)
            keyboard.press_and_release('tab')

            keyboard.press_and_release('ctrl+a')
            keyboard.press_and_release('8')
            
            time.sleep(x)
            keyboard.press_and_release('tab')
            time.sleep(x)
            keyboard.press_and_release('ctrl+a')
            time.sleep(x)
            pyperclip.copy(row[7])
            keyboard.press_and_release('ctrl+v')
            time.sleep(x)
            keyboard.press_and_release('tab')
            time.sleep(x)
            
            pyperclip.copy(row[3])
            time.sleep(x)
            keyboard.press_and_release('ctrl+a')
            time.sleep(x)
            keyboard.press_and_release('ctrl+v')
            time.sleep(x)
            
            if row[9]=="1.5":            
                keyboard.press_and_release('tab')
                time.sleep(x)
                pyperclip.copy("gr. 1,5 mm")
                time.sleep(x)
                keyboard.press_and_release('ctrl+a')
                time.sleep(x)
                keyboard.press_and_release('ctrl+v')
                time.sleep(x)
            
            if row[10]=="nie":#certyfikacja i na koncu folia
                keyboard.press_and_release('tab')
                time.sleep(x)
                pyperclip.copy("TYP" + str(row[2]))
                time.sleep(x)
                keyboard.press_and_release('ctrl+a')
                time.sleep(x)
                keyboard.press_and_release('ctrl+v')
                time.sleep(x)
                
            
            
        
            keyboard.press_and_release('enter')
            time.sleep(x)
            pyperclip.copy(row[0])
            time.sleep(x)
            
            keyboard.press_and_release('ctrl+v')
            time.sleep(x)
            keyboard.press_and_release('enter')
            
            
        time.sleep(1)
        subprocess.call(('taskkill', '/F', '/IM', 'etiLABEL.exe'))
    print("koniec")
    for item_id in tree.get_children():
        tree.delete(item_id)   
#endregion     
        
root = tk.Tk()
root.title("Drukowanie")




frame_buttons = tk.Frame(root, bg="white" ,height=150)
frame_buttons.grid(row=3, column=0, columnspan=6,rowspan=2, sticky="ew")

bez_certyfikat_button_var = tk.BooleanVar()
bez_certyfikat_button_var.set(False)
bez_certyfikat_button = tk.Button(root, text="BEZ CERTYFIKARU", relief=tk.RAISED, command=wybierz_bez_certyfikatu, highlightthickness=0)
bez_certyfikat_button.grid(row=3, column=4, padx=5, pady=5,columnspan=2)











#region zmienne przypisane do podstawowych przyciskow
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

#endregion

#region podstawowe przyciski
# Przyciski ZKS, ZKP i Inne
zks_button = tk.Button(root, text="ZKS", relief=tk.RAISED, command=wybierz_zks, highlightthickness=0)
zkp_button = tk.Button(root, text="ZKP", relief=tk.RAISED, command=wybierz_zkp, highlightthickness=0)
inne_button = tk.Button(root, text="Inne", relief=tk.RAISED, command=wybierz_inne, highlightthickness=0)

# Pole tekstowe dla przycisku "Inne"
tekst_entry_inne = tk.Entry(root, width=5, state=tk.DISABLED)  # Ograniczenie pola tekstowego do pięciu liter

# Pole tekstowe dla końcówki tekstu
tekst_entry_koncowka = tk.Entry(root, width=10,font=("Helvetica", 20))

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

#endregion

# Przycisk "Dodaj"
dodaj_button = tk.Button(root, text="Dodaj", command=dodajDoTabeli)

# SYMBOL
symbol_napis = tk.Label(root, text="SYMBOL:",font=("Helvetica", 12))
symbol_napis.grid(row=6, column=0, padx=5, pady=5)

pole_nazwy_znaku = tk.Entry(root, width=10,font=("Helvetica", 12))
pole_nazwy_znaku.bind("<Return>", funkcja_po_enter)
pole_nazwy_znaku.grid(row=6, column=1, padx=5, pady=5)

#ROZMIAR
rozmiar_napis = tk.Label(root, text="ROZMIAR:",font=("Helvetica", 12))
rozmiar_napis.grid(row=6, column=2, padx=5, pady=5)

pole_rozmiaru_znaku = tk.Entry(root, width=10,font=("Helvetica", 12))
pole_rozmiaru_znaku.grid(row=6, column=3, padx=5, pady=5)

#ILOSC
ilosc_napis = tk.Label(root, text="ILOSC",font=("Helvetica", 12))
ilosc_napis.grid(row=6, column=4, padx=5, pady=5)

pole_ilosc_wimedek = tk.Entry(root, width=10,font=("Helvetica", 12))
pole_ilosc_wimedek.grid(row=6, column=5, padx=5, pady=5)






#region grid przyciski
zks_button.grid(row=0, column=0, padx=5, pady=5)
zkp_button.grid(row=0, column=1, padx=5, pady=5)
inne_button.grid(row=0, column=2, padx=5, pady=5)
tekst_entry_inne.grid(row=0, column=3, padx=5, pady=5)
tekst_entry_koncowka.grid(row=0, column=4, padx=5, pady=5)

folia1_button.grid(row=1, column=0, padx=5, pady=5)
folia2_button.grid(row=1, column=1, padx=5, pady=5)
folia3_button.grid(row=1, column=2, padx=5, pady=5)

ocynk_button.grid(row=2, column=1, padx=5, pady=5,)
aluminum_button.grid(row=2, column=0, padx=5, pady=5,)
przycisk_125.grid(row=2, column=2, padx=5, pady=5)
przycisk_150.grid(row=2, column=3, padx=5, pady=5)

profil_button.grid(row=3, column=0, padx=5, pady=5)
bez_profilu_button.grid(row=3, column=1, padx=5, pady=5)

czarny_button.grid(row=3, column=2, padx=5, pady=5,)
bez_czarnego_button.grid(row=3, column=3, padx=5, pady=5,)

kwadrat_button.grid(row=4, column=0, padx=5, pady=5)
prostokat_button.grid(row=4, column=1, padx=5, pady=5)
trojkat_button.grid(row=4, column=2, padx=5, pady=5)
romb_button.grid(row=4, column=3, padx=5, pady=5)
osmiokat_button.grid(row=4, column=4, padx=5, pady=5)
kolo_button.grid(row=4, column=5, padx=5, pady=5)
#endregion



dodaj_button.grid(row=8, column=5, columnspan=1, padx=5, pady=10)  # Button ma columnspan=5, aby rozciągnąć się przez cały rzęd





# Przycisk "Usuń"

usun_button = tk.Button(root, text="Usuń", command=usun_zaznaczone)
usun_button.grid(row=8, column=6, padx=5, pady=10)


drukuj_wszystko_button = tk.Button(root, text="Drukuj wszystko", command=drukuj_wszystko)
drukuj_wszystko_button.grid(row=9, column=6, padx=5, pady=10)


# Tabela po prawej stronie
tree = ttk.Treeview(root, columns=("ilosc","Button", "Text", "Blacha", "Profil", "Kształt", "Kolor", "Symbol", "Rozmiar", "1.25/1.5"))
# Ustaw szerokość kolumny numer 1 na 20 pikseli
for col in ("#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9","#10"):
    tree.column(col, width=50)


tree.heading("#1", text="ilosc wimedek:")
tree.heading("#2", text="NR_ZAMÓWIENIA")
tree.heading("#3", text="FOLIA")
tree.heading("#4", text="ROZMIAR")
tree.heading("#5", text="PROFIL")
tree.heading("#6", text="KSZTAŁT")
tree.heading("#7", text="KOLOR")
tree.heading("#8", text="SYMBOL")
tree.heading("#9", text="RODZAJ_BLACHY")
tree.heading("#10", text="GRUBOŚĆ_BLACHY")

tree.grid(row=0, column=6, rowspan=5, padx=0, pady=0)



u6a_button = tk.Button(root, text="U6a", command=set_u6a_bez_czarnego_prostokat)
u6a_button.grid(row=9, column=2, padx=5, pady=5)

e15_button = tk.Button(root, text="E15", command=set_e15_prostokat_z_czarnym)
e15_button.grid(row=9, column=3, padx=5, pady=5)

g1_button = tk.Button(root, text="G1", command=set_g1_bez_czarnego_prostokat)
g1_button.grid(row=9, column=1, padx=5, pady=5)

u3a_button = tk.Button(root, text=" U3a", command=set_u3a_and_size)
u3a_button.grid(row=9, column=0, padx=5, pady=1)

b43_button = tk.Button(root, text="B43", command=set_B43)
b43_button.grid(row=8, column=0, padx=5, pady=1)

b44_button = tk.Button(root, text="B44", command=set_B44)
b44_button.grid(row=8, column=1, padx=5, pady=1)

D18a_button = tk.Button(root, text="D18a", command=set_D18a)
D18a_button.grid(row=8, column=2, padx=5, pady=1)



wybierz_ocynk()
wybierz_zks()
wybierz_125()

"""
#region skroty klawiszowe:
keyboard.add_hotkey('shift+1', wybierz_folia1)
keyboard.add_hotkey('shift+2', wybierz_folia2)
keyboard.add_hotkey('shift+3', wybierz_folia3)

keyboard.add_hotkey('shift+f', wybierz_profil)
keyboard.add_hotkey('shift+g', wybierz_bez_profilu)

keyboard.add_hotkey('shift+c', wybierz_z_czarnym)
keyboard.add_hotkey('shift+v', wybierz_z_czarnym)
keyboard.add_hotkey('shift+v', wybierz_bez_czarnego)

keyboard.add_hotkey('shift+space', dodajDoTabeli)
keyboard.add_hotkey('shift+alt', drukuj_wszystko)
"""
all_entry = [pole_ilosc_wimedek,pole_rozmiaru_znaku,pole_nazwy_znaku,tekst_entry_koncowka]
"""
def po_odpuszczeniu_shift(e):
    if e.name == 'shift':
        for i in range(len(all_entry)):
            if len(all_entry[i].get()) == 0:
                all_entry[i].focus_set()
keyboard.on_release(po_odpuszczeniu_shift)
"""



def styl_przyciskow():
    all_buttons = [
    zks_button, zkp_button, inne_button, folia1_button, folia2_button, folia3_button,
    ocynk_button, aluminum_button, profil_button, bez_profilu_button, kwadrat_button,
    prostokat_button, trojkat_button, romb_button, osmiokat_button, kolo_button,
    czarny_button, bez_czarnego_button, przycisk_125, przycisk_150, dodaj_button,
    usun_button, drukuj_wszystko_button, u6a_button, e15_button, g1_button, u3a_button, D18a_button,bez_certyfikat_button,b44_button,b43_button,
    ]
    for button in all_buttons:
          button.config(font=("Arial", 13))
          #button.grid_configure(padx=0)
    
    

# Collect all buttons into a list

def insetring_data_from_csv(wiersz):
    pattern = r"(?:ZNAK|TABLICA\/U\/3\/[AB]|TABLICZKA).*\/[0-9x]*\/(?:OCO|AL)\/(?:1,25|1,5)\/(?:NM|M)\/K\/(?:F|0)\/(?:1|2|3)"
    if re.search(pattern,wiersz[5]):
        
        znak = wiersz[5].split("/")
        del znak[0]
        print(znak)
        
        #folia
        print(znak[-1])
        if str(znak[-1]).startswith("1"):
            wybierz_folia1()
        if str(znak[-1]).startswith("2"):
            wybierz_folia2()
        if str(znak[-1]).startswith("3"):
            wybierz_folia3()
        del znak[-1]     
        #profil
               
        if znak[-1] == "F":
            wybierz_profil()
        if znak[-1] == "0":
            wybierz_bez_profilu()
        del znak[-1]
        
        #klejony        
        del znak[-1]
           
        #malowanie
        print(znak[-1])
        if znak[-1] == "NM":
            wybierz_bez_certyfikatu()
        del znak[-1]
        
        #grubosc
        if znak[-1] == "1,25":
            wybierz_125()
        if znak[-1] == "1,5":
            wybierz_150()
        del znak[-1]
        
        #ocynko al
        if znak[-1] == "OCO":
            wybierz_ocynk()
        if znak[-1] == "AL":
            wybierz_aluminum()
        del znak[-1]
        
        pole_rozmiaru_znaku.delete(0, tk.END)
        pole_rozmiaru_znaku.insert(0, znak[-1])
        del znak[-1]
        
        pole_nazwy_znaku.delete(0, tk.END)
        #pole_nazwy_znaku.insert(0, str(znak).strip("[").strip("]").strip(",").strip("'"))
        pole_nazwy_znaku.insert(0,str(str(znak[0]) + str(znak[1])))
        
        
        
        
    
        
        return True
    return False
    
    
    
    
#test 
dd = "ZNAK/C/16A/13A/PION/600/OCO/1,5/M/K/F/3"
insetring_data_from_csv(['ZKS/000497/2024/009/000080', '792509', 'PIS', '2024-01-24 10:29:03', '2024-01-30 00:00:00', dd, 'szt', 'KT/2016/009089', 'ZKS/000497/2024'])
def next_position():
    pom =  csv_pozycja.get()
    pom = pom.strip()
    pom = int(pom)
    pom = pom + 1
    csv_pozycja.delete(0, tk.END)
    csv_pozycja.insert(0, pom)
    
def csv_pobieranie():
    wiersz = "" 
    pozycja = Entry_Do_csv.get()+"/"+csv_pozycja.get().zfill(3)
    #pozycja = "ilosc_pustki/006"
    ilosc_pustki = csv_pozycja.get().count(" ")
    print(ilosc_pustki)
    if ilosc_pustki == 3:
        next_position()        
        dodajDoTabeli()
        print("nest")
    elif ilosc_pustki == 2:
        
        funkcja_po_enter(0)
        
        print("rozpoznajer")
    elif ilosc_pustki == 1:
        
        print("wpisuje")
        
    else:
        print("szukam CSV")
        with open(f"C:\\Users\\eninq\\Desktop\\wimedki_kompdolny\\zlecenia.csv", newline='', encoding='ISO-8859-1') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=';')
           
                for row in csvreader:
                    if pozycja in row[0]:
                        print(row[5])
                        wiersz = row                
        if wiersz == "":
            print("ide dalej nic tu nie ma")
            next_position()
        else:
            print(wiersz)
            operacja = insetring_data_from_csv(wiersz)
            if operacja == False:
                next_position()
        
    

Entry_Do_csv = tk.Entry(root, width=15,font=("Helvetica", 20))
Entry_Do_csv.grid(row=12, column=0,columnspan=2, padx=5, pady=5)

csv_pozycja = tk.Entry(root, width=10,font=("Helvetica", 20))
csv_pozycja.grid(row=12, column=3, padx=5, pady=5)
keyboard.add_hotkey('shift+Space', csv_pobieranie)

# Call the function with the list of buttons and the desired height
styl_przyciskow()
root.mainloop()

import tkinter as tk

def wybierz_kwadrat():
    if wybrana_proporcja.get() == "3x3":
        entry_3x3.config(state=tk.NORMAL)
        label_akcja_3x3.config(foreground="blue")  # Zmiana koloru etykiety dla wizualnej informacji
    else:
        entry_3x3.config(state=tk.DISABLED)
        label_akcja_3x3.config(foreground="black")  # Przywrócenie koloru etykiety

def akcja_po_kliknieciu():
    print("Akcja po kliknięciu w nieaktywne pole!")

root = tk.Tk()

wybrana_proporcja = tk.StringVar(value=None)

ratio_600 = tk.Radiobutton(root, text="600x600", variable=wybrana_proporcja, value="600x600", command=wybierz_kwadrat)
ratio_600.grid(row=10, column=1, padx=10, pady=10)

ratio_44x44 = tk.Radiobutton(root, text="44x44", variable=wybrana_proporcja, value="44x44", command=wybierz_kwadrat)
ratio_44x44.grid(row=10, column=2, padx=10, pady=10)

ratio_3x3 = tk.Radiobutton(root, text="3x3", variable=wybrana_proporcja, value="3x3", command=wybierz_kwadrat)
ratio_3x3.grid(row=10, column=3, padx=10, pady=10)

entry_3x3 = tk.Entry(root, state=tk.DISABLED)  # Pole tekstowe domyślnie wyłączone
entry_3x3.grid(row=11, column=3, padx=10, pady=10)

label_akcja_3x3 = tk.Label(root, text="Kliknij mnie!", cursor="hand2")
label_akcja_3x3.grid(row=12, column=3, padx=10, pady=10)
label_akcja_3x3.bind("<Button-1>", lambda event: akcja_po_kliknieciu())

root.mainloop()

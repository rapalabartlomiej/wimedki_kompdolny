if pierwsza_litera =="D":
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
           
import random

def wypelnij_tablice(tablica, rozmiar):
    for i in range(rozmiar):
        tablica.append(random.randint(1, 100))

def znajdz_liczbe(tablica, rozmiar, szukana):
    tablica.append(szukana)
    for i in range(rozmiar):
        if tablica[i] == szukana:
            return i
    return -1

def wypisz_tablice(tablica, rozmiar, szukana):
    znaleziona = znajdz_liczbe(tablica, rozmiar, szukana)
    for i in range(rozmiar):
        print(tablica[i], end=", ")
    print()

    if znaleziona == -1:
        print(f"Nie znaleziono liczby {szukana} w tablicy")
    else:
        print(f"Znaleziono szukaną na indeksie: {znaleziona}")


rozmiar = 50
tablica = []

wypelnij_tablice(tablica, rozmiar)
szukana = int(input("Jaka liczbe chcesz znalezc: "))
wypisz_tablice(tablica, rozmiar, szukana)








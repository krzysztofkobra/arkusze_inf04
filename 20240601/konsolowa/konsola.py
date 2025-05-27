from random import randint

def losowanie(liczba_rzutow):
        wylosowane = {1: 0, 2 : 0, 3: 0, 4 : 0, 5 : 0, 6 : 0}
        losowania = []

        for i in range(liczba_rzutow):
            losowa = randint(1, 6)
            wylosowane[losowa] += 1
            losowania.append(losowa)

        for i in range(len(losowania)):
            print(f"Kostka {i+1}: {losowania[i]}")

        return wylosowane

def zliczanie(wylosowane):
    wynik = 0
    for liczba_oczek, liczba_wylosowan in wylosowane.items():
        if liczba_wylosowan > 1:
            wynik += liczba_oczek * liczba_wylosowan

    print(f"Liczba uzyskanych punktów: {wynik}")


def program():
    wybor = "t"

    liczba_rzutow = int(input("Ile kostek chcesz rzucić?(3 - 10) \n"))
    while liczba_rzutow < 3 or liczba_rzutow > 10:
        liczba_rzutow = int(input("Ile kostek chcesz rzucić?(3 - 10) \n"))

    while(wybor == "t"):
        wylosowane = losowanie(liczba_rzutow)
        zliczanie(wylosowane)

        wybor = input("Jeszcze raz? (t/n) \n")
        if wybor == "t":
            pass
        elif wybor == "n":
            break

program()
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from styl import Ui_Form
from random import randint

class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.s = Ui_Form()
        self.s.setupUi(self)

        self.wynik_calkowity = 0

        self.s.rzut.clicked.connect(self.losowanie)
        self.s.reset.clicked.connect(self.reset)


    def losowanie(self):
        wylosowane = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        losowania = []

        kosci = [self.s.kosc1, self.s.kosc2, self.s.kosc3, self.s.kosc4, self.s.kosc5]
        obrazy = ["pliki/k1.jpg","pliki/k2.jpg","pliki/k3.jpg",
                  "pliki/k4.jpg","pliki/k5.jpg","pliki/k6.jpg", "pliki/question.jpg"]

        for i in range(5):
            losowa = randint(1, 6)
            wylosowane[losowa] += 1
            losowania.append(losowa)

        for i in range(5):
            kosci[i].setPixmap(QPixmap(obrazy[losowania[i]-1]))

        wynik_losowania = 0
        for liczba_oczek, liczba_wylosowan in wylosowane.items():
            if liczba_wylosowan > 1:
                wynik_losowania += liczba_oczek * liczba_wylosowan

        self.wynik_calkowity += wynik_losowania
        self.s.wynik_tego_losowania.setText(f"Wynik tego losowania: {wynik_losowania}")
        self.s.wynik_gry.setText(f"Wynik gry: {self.wynik_calkowity}")

    def reset(self):
        kosci = [self.s.kosc1, self.s.kosc2, self.s.kosc3, self.s.kosc4, self.s.kosc5]

        self.wynik_calkowity = 0
        for i in range(5):
            kosci[i].setPixmap(QPixmap("pliki/question.jpg"))

        self.s.wynik_tego_losowania.setText(f"Wynik tego losowania: 0")
        self.s.wynik_gry.setText(f"Wynik gry: {self.wynik_calkowity}")

app = QApplication([])
okno = Okno()
okno.show()
app.exec_()
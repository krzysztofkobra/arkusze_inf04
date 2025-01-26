#include <iostream>

using namespace std;

class Osoba{
    public:
        Osoba(){
            id = 0;
            imie = "";
            liczbaInstancji++;
        }
        
        Osoba(int id, string imie): id(id), imie(imie) {
            liczbaInstancji++;
        }

        Osoba(const Osoba& osoba){
            id = osoba.id;
            imie = osoba.imie;
            liczbaInstancji++;
        }
        
        // const string& drugieImie - można też tak, tak samo w konstuktorach, jest to oszczedniejsze dla pamieci, 
        // bo nie tworzymy kopii obiektu tylko przekazujemy jego wartosc, ale na egzaminie lepiej jest pisac prostym kodem
        void wypisz_imie(string drugieImie){  
            if(imie.empty()){
                cout << "Brak danych" << endl;
            }
            else{
                cout << "Czesc " << drugieImie << ", mam na imie " << imie << endl;
            }
        }

        static int liczbaInstancji;
    private:
        int id;
        string imie;
};

int Osoba::liczbaInstancji = 0;

int main()
{
    Osoba o1;
    Osoba o2(1, "Jan");
    Osoba o3(o2); // Osoba o3 = o2; jest rownie z popawne

    std::cout << "Liczba instancji: " << Osoba::liczbaInstancji << std::endl;

    o1.wypisz_imie("Piotr");
    o2.wypisz_imie("Darek");
    o3.wypisz_imie("Marek");

    return 0;
}
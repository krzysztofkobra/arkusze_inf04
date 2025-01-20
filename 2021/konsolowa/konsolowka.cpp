#include <iostream>

using namespace std;

class Tablice{
    private:
        int tablica[10];
        int znajdz_najwyzsza_wartosc(); // nie wiem czy mamy to gdzieś użyć/wywołać, można na pewno było z tego skorzystać w metodzie sortowania
    public:
        void sortuj_przez_wybor();
        void wypełnij_tablice();
        void wyswietl_tablice();
};

void Tablice::sortuj_przez_wybor(){
    for(int i = 9; i > 0; i--){
        for(int j = i-1; j >= 0; j--){
            if(tablica[j]<tablica[i]){
                swap(tablica[j], tablica[i]);
            }
        }
    }
}

int Tablice::znajdz_najwyzsza_wartosc(){
    int najwyzsza = tablica[0];
    for(int i = 1; i < 10; i++){
        if(tablica[i] > najwyzsza){
            najwyzsza = tablica[i];
        }
    }
    return najwyzsza;
}

void Tablice::wypełnij_tablice(){
    cout << "Podaj 10 liczb całkowitych do tablicy: \n";
    for(int i = 0; i < 10; i++){
        cin >> tablica[i];
    }
}

void Tablice::wyswietl_tablice(){
    for(int i = 0; i < 10; i++){
        cout << tablica[i] << " ";
    }
}

int main()
{
    Tablice t;
    t.wypełnij_tablice();
    t.sortuj_przez_wybor();
    t.wyswietl_tablice();
    return 0;
}
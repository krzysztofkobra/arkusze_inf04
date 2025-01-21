#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int znajdz_element(int tab[], int n, int x){
    tab[n] = x;
    for(int i = 0; i < n; i++){
        if(tab[i] == x){
            return i;
        }
    }
    return -1;
}

void wypelnij_tablice(int tab[], int n){
    for(int i = 0; i < n; i++){
        tab[i] = rand() % 100 + 1;
    }
}

void wyswietl_tablice(int tab[], int n, int szukana){
    int znaleziona = znajdz_element(tab, n, szukana);
    for(int i = 0; i < n; i++){
        cout << tab[i];
        if (i < n - 1) {
            cout << ",";
        }
    }
    if(znaleziona == -1)
        cout << "\n Element " << szukana << " nie istnieje w tablicy.";
    else
        cout << "\n Znaleziony element jest pod indeksem: " << znaleziona;
    
    
}

int main(){
    int rozmiar = 50;

    int tablica[rozmiar+1];
    wypelnij_tablice(tablica, rozmiar);

    int szukana;
    cout << "Podaj szukana liczbe: ";
    cin >> szukana;
    cout << endl;

    wyswietl_tablice(tablica, rozmiar, szukana);

    return 0;
}
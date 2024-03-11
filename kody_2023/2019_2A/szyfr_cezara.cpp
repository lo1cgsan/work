/*
 * szyfr_cezara.cpp
 */
#include <iostream>
using namespace std;

void male_litery(char t[]) {
    int i = 0;
    while (t[i] != '\0'){
        if ((int)t[i] > 64 && (int)t[i] < 91) {
            t[i] = (char)((int)t[i] + 32);
        }
        i++;
    }
}

void szyfruj(char t[], int k) {
    int i = 0;
    int kod = 0;
    while (t[i] != '\0'){
        kod = (int)t[i] + k;
        if (kod > 122) {
            kod -= 26;
        }
        t[i] = (char)kod;
        i++;
    }
}

void deszyfruj(char t[], int k) {
    int i = 0;
    int kod = 0;
    while (t[i] != '\0'){
        kod = (int)t[i] - k;
        if (kod < 97) {
            kod += 26;
        }
        t[i] = (char)kod;
        i++;
    }
}

int main(int argc, char **argv)
{
    int r = 100;
    char tekst[r];
    cout << "Podaj tekst:" << endl;
    cin.getline(tekst, r);
    male_litery(tekst);
    int klucz = 0;
    cout << "Podaj klucz:" << endl;
    cin >> klucz;
    klucz = klucz % 26;
    szyfruj(tekst, klucz);
    cout << tekst << endl;
    deszyfruj(tekst, klucz);
    cout << tekst << endl;
    
    return 0;
}


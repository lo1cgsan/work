/*
 * anagramy.cpp
 */


#include <iostream>
#include <cstring>

using namespace std;

bool czy_palindrom(char tab[]) {
    int rozmiar = strlen(tab);
    cout << rozmiar << endl;
    int i = 0;
    for(i = 0; i < rozmiar / 2; i++) {
        cout << tab[i] << "\t" << tab[rozmiar - 1 - i] << endl;
        if (tab[i] == tab[rozmiar - 1 - i])
            ;
        else
            return false;
    }
    return true;
}


void removeSpaces(char tab1[], char tab2[]) {
    int rozmiar = strlen(tab1);
    cout << rozmiar << endl;
    int i = 0;
    for(i = 0; i < rozmiar; i++) {
        if (tab1[i] == ' ') {
            tab2[i] = tab1[i];
        }
    }
    tab2[i] = '\0';
}


bool czy_palindrom2(char tab[]) {
    
    int rozmiar = strlen(tab);
    for(int i = 0; i < rozmiar / 2; i++) {
        if (tab[i] == tab[rozmiar - 1 - i])
            ;
        else
            return false;
    }
    return true;
}

int main(int argc, char **argv)
{

    int r = 20;
	char napis1[r];
    char napis2[r];
    cin.getline(napis1, 20);
    removeSpaces(napis1, napis2);
    
    if (czy_palindrom(napis2)) {
        cout << "To palindrom!" << endl;
    } else {
        cout << "To nie palindrom!" << endl;
    }
       
	return 0;
}


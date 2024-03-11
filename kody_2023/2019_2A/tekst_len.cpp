/*
 * znaki.cpp
 * znakiem kończącycm tablicę znakową jest \0
 */


#include <iostream>
#include <cstring>

#define MAX_R 100

using namespace std;

int main(int argc, char **argv)
{
    char tekst[MAX_R];
    cout << "Podaj tekst:" << endl;
    cin.getline(tekst, MAX_R);
    cout << strlen(tekst) << endl;
    
    return 0;
}


/*
 * euklides.cpp
 */

#include <iostream>
using namespace std;

int nwd_1(int a, int b) {
    int i = 0;
    while (a != b) {
        i++;
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }
    cout << "NWD: " << a << endl;
    cout << "Powtórzeń: " << i << endl;
    return a;
}

int nwd_2(int a, int b) {
    int i = 0;
    while (a > 0) {
        i++;
        a = a % b;
        b = b - a;
    }
    cout << "NWD: " << b << endl;
    cout << "Powtórzeń: " << i << endl;
    return b;
}

// NWD(a, b) = b dla a = 0
// NWD(a, b) = { a = a % b; b = b - a; }
// NWD(a, b) = NWD(a % b,  b - a)
int NWD_re1(int a, int b) {
    if (a != 0)
        return NWD_re1(a % b, b - (a % b));
    else
        return b;
}

// NWD(a, b) = a dla b = 0
// NWD(a, b) = {a = b, b = a % b}
// NWD(a, b) = NWD(b, a % b)
int NWD_re2(int a, int b) {
    if (b != 0)
        return NWD_re2(b, a % b);
    else
        return a;
}
// napisz iteracyjną wersję funkcji NWD_re2


int main(int argc, char **argv)
{
    int a, b, i;
    a = b = i = 0;
    cout << "Podaj dwie liczby całkowite: " << endl;
    cin >> a >> b;
    nwd_1(a, b);
    nwd_2(a, b);
    cout << NWD_re1(a, b) << endl;
    cout << NWD_re2(a, b) << endl;
    return 0;
}


/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;

// x0 = 1 dla x=/0
// x1 = x
// xn = x * ... * x(n-czynników)

float potega_it(float x, int n) {
    float potega = 1;
    for (int i=0; i < n; i++) {
        potega = potega * x;
    }
    return potega;
}

// x0 = 1 dla x=/0
// xn = x(n-1) * x, n > 0

float potega_re(float x, int n) {
    if (n == 0)
        return 1;
    else
        return potega_re(x, n-1) * x;
}

//~potega_re(2, 4);
//~potega_re(2, 3) * 2;
//~potega_re(2, 2) * 2;
//~potega_re(2, 1) * 2;
//~potega_re(2, 0) = 1;
//~1 * 2 = 2;
//~2 * 2 = 4;
//~4 * 2 = 8;
//~8 * 2 = 16;

int main(int argc, char **argv)
{
	float x;  // podstawa
    int n;  //wykładnik
    cout << "Podaj podstawę: " << endl;
    cin >> x;
    cout << "Podaj wykładnik: " << endl;
    cin >> n;
    cout << "Potęga: " << potega_it(x, n) << endl;
    cout << "Potęga: " << potega_re(x, n) << endl;
	return 0;
}


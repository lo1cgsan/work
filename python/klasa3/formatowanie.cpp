/*
 * formatowanie.cpp
 */

#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdio>

using namespace std;

int main(int argc, char **argv)
{
    
    int li = 100;
    float lf = 12.760;
    
    cout << endl;
    cout.precision(5);
    cout.width(20);
    cout << lf << endl;
    cout << setprecision(10) << setw(15) << M_PI << endl;
    cout << showbase << hex << li << endl;
    cout << showbase << oct << li << endl;

    printf("%10.4f\n", M_PI);
    printf("%10.4f\n", (double)li);
    printf("Hex: %#x\n", li);
    printf("Oct: %#o\n", li);
    return 0;
}


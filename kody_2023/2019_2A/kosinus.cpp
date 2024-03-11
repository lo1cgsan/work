/*
 * kosinus.cpp
 */
#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char **argv)
{
    float stopien, radian;
    stopien = 0.0;
    //~cout << cos(90 * M_PI / 180) << endl;
    //~return 0;
    do {
        radian = stopien * M_PI / 180;
        cout << "cos(" << stopien << ")" << cos(radian) << endl;
        stopien += 10.0;
    } while (stopien <= 90.0);
	return 0;
}


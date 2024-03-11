/*
 * anagramy.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    // n! = 1 * ... * n
    // n! = (n-1)! * n

    int r = 4;
	char napis[]="krab";
    int i1, i2, i3, i4;
    i2 = 1; i3 = 2; i4 = 3;
    for (i1=0; i1 < r; i1++) {
        for (i2=0; i2 < r; i2++) {
            if (i2 == i1) continue;
            for (i3=0; i3 < r; i3++) {
                if (i3 == i2 || i3 == i1) continue;
                for (i4=0; i4 < r; i4++) {
                    if (i4 == i1 || i4 == i2 || i4 == i3) continue;
                    cout << napis[i1] << napis[i2] << napis[i3] << napis[i4] << endl;
                }
            }
        }
    }
    
	return 0;
}


/*
 * parzyste.cpp
 * Program powinien wydrukować liczby parzyste z przediału [0, 100]
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	//~[0, 100]
    int i = 0;
    for (i = 0; i <= 100; i += 2) {
        cout << i << " ";
    }
	return 0;
}


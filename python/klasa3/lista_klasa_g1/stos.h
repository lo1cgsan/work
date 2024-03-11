#ifndef _STOS_H_
#define _STOS_H_

#include "lista.h"

class Stos {
    private:
        Lista lista;
    public:
        void Push(int);
        int Pop();
        bool Pusty();
};

#endif

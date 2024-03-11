#ifndef _LISTA_H_
#define _LISTA_H_

typedef struct ELEMENT{
    int value;
    ELEMENT *next;
}ELEMENT;

typedef struct HEADER{
    ELEMENT *head;
    ELEMENT *tail;
}HEADER;

class Lista {
    private:
        HEADER header;
    public:
      Lista();  // konstruktor
      ~Lista();  // destruktor
      void Dodaj(int value);
      bool Wstaw(int value, int position);
      int Usun();
      bool Usun(int);
      void Wyswietl();
      bool Pusta();
};

#endif

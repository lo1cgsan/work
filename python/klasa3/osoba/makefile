CXX=g++
CXXFLAGS=-Wall -I.
OBJS=osoba.o osoby.o

pong: osoba.o osoby.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o osoby.exe

.PHONY: clean

clean:
	rm -f *.o *.exe *~ core *~

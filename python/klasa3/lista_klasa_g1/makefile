CXX=g++
CXXFLAGS=-Wall -I.
OBJS=lista.o stos.o main.o

pong: lista.o stos.o main.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o main.exe

.PHONY: clean

clean:
	rm -f *.o *.exe *~ core *~

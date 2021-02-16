PA1: BlockCipher.o StreamCipher.o main.o
	g++ -Wall -I. -std=c++11 BlockCipher.o StreamCipher.o main.o -o PA1
BlockCipher.o: BlockCipher.cc BlockCipher.h
	g++ -Wall -I. -std=c++11 -c BlockCipher.cc
StreamCipher.o: StreamCipher.cc StreamCipher.h
	g++ -Wall -I. -std=c++11 -c StreamCipher.cc
main.o: main.cc BlockCipher.h StreamCipher.h
	g++ -Wall -I. -std=c++11 -c main.cc

clean:
	rm *.o PA1
	
tar:
	tar -cvf PA1.tar *.cpp *.h Makefile
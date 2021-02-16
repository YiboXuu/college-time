# List of files
C_SRCS = Starter.c Red.c Green.c Blue.c
C_OBJS = Starter.o Red.o Green.o Blue.o
#C_HEADERS
OBJS = ${C_OBJS}
EXE = Starter
EXE1 = Red
EXE2 = Green
EXE3 = Blue
#Compiler and loader commands and flags
# -g : generates default debug info.
# -Wall: enables all compiler warnings
# -c: compiles source files without linking.
# -I: Include directory of header files.
GCC = gcc
GCC_FLAGS = -std=c11 -g -Wall -c -I.
LD_FLAGS = -std=c11 -g -Wall -I.

#Compile .c files to .o files
.c.o:
	$(GCC) $(GCC_FLAGS) $<
#Target is the executable
build: Starter Red Green Blue
Starter: Starter.o
	$(GCC) $(LD_FLAGS) Starter.o -o $(EXE)
Red: Red.o
	$(GCC) $(LD_FLAGS) Red.o -o $(EXE1)
Green: Green.o
	$(GCC) $(LD_FLAGS) Green.o -o $(EXE2)
Blue: Blue.o
	$(GCC) $(LD_FLAGS) Blue.o -o $(EXE3)
	
#Recompile C objects if headers change
$(C_OBJS): ${C_HEADERS}
#Clean up the directory
clean:
	rm -f *.o *~ $(EXE) $(EXE1) $(EXE2) $(EXE3)
package:
	tar -cvzf $(name) *.c *.txt Makefile
	tar -cvzf $(name) *.c *.txt Makefile


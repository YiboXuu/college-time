# List of files
C_SRCS = scheduler.c 
C_OBJS = scheduler.o 
#C_HEADERS
OBJS = ${C_OBJS}
EXE = scheduler

GCC = gcc
GCC_FLAGS = -std=gnu99 -g -Wall -c -I. 
LD_FLAGS = -std=gnu99 -g -Wall -I. 


.c.o:
	$(GCC) $(GCC_FLAGS) $<

build: scheduler 
scheduler: scheduler.o
	$(GCC) $(LD_FLAGS) scheduler.o -o $(EXE)

	
#Recompile C objects if headers change
$(C_OBJS): ${C_HEADERS}
#Clean up the directory
clean:
	rm -f *.o *~ $(EXE) $(EXE1) $(EXE2) $(EXE3) $(EXE4)
package:
	tar -cvzf $(name) *.c *.txt makefile
	


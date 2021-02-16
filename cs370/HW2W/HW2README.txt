README
======

A. This package includes the following files. In your own readme file, modify the information as needed.

|-- Starter.c
|-- red.c
|-- blue.c
|-- green.c
|-- HW2.PDF
|-- makefile
|-- README.txt 


B. Use your designed makefile 
To compile the code and build the executable using the command 

systemprompt>  make

To remove the  executable files use

systemprompt>  make clean

To run the program use 

systemprompt> ./Starter

which will run the program and generate the outputs.


C. Answer the following questions 

uestions: 
1.How many of the least significant bits of the status does WEXITSTATUS return?
			8 bits from 0-255
		


2.Which header file has to be included to use the WEXITSTATUS? 
		#include <sys/wait.h>


 
3.What is the return value for the fork() in a child process?  
		fork() returns 0 to the child process.
		
4.Give a reason for the fork() to fail?  
		lack of available resources;


5.In the program written by you, are we doing a sequential processing or 
a concurrent processing withrespect to the child processes? 
Sequential processing is when only one of the child processes is 
running at one time, and concurrent processing is when more than one child process
can be running at the same time. 

		we are doing a sequential processing.
  
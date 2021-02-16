README
======

A. This package includes the following files.

|-- Starter.c
|-- FileReader.c
|-- red.c
|-- blue.c
|-- green.c
|-- HW3.PDF
	The description of our this time homwork.
|-- makefile
|-- README.txt 


B. Use your designed makefile 
To compile the code and build the executable using the command 

systemprompt>  make

To remove the  executable files use

systemprompt>  make clean

To run the program use 

systemprompt> ./Starter
	      ./Starter coded__image_2.txt
which will run the program and generate the outputs.


C. Answer the following questions 

1. Name the function that is used to create a pipe. Which ends denotes the read and the write
ends of a pipe? (2 points)
	pipe() function that is used to create a pipe.
	
	fd[0] for reading and fd[1] for writing. In my code this is array[0] array[1]

2. Name the function used to map files or devices in to memory? (1 point)

			mmap
			This function maps the memory object into memory.
3. Name the function used to open a shared memory object? What does it return? (2 points)
		
		shm_open that function used to open a shared memory.
		shm_open function returns a file descriptor that is associated with 					the shared "memory object" specified by name. 
    

README
======

A. This package includes the following files.

|-- Coordinator.java
	That function contain the main function that created producer and consumer, also contain 
	the getTime function that we can used in the Producer.java and Consumer.java.The consumer might 
	be multiple.
|-- Producer.java	
	The producer.java insert the random number (used seed) into the buffer after checking 
	that is full or not, the medthod is in Buffer.java. If buffer is full, wait() others to remove it.
|-- Consumer.java
	The consumer.java check the buffer is empty or not, if that is not empty, remove the number 
	from the buffer, else wait the other function insert the function.
|-- Buffer.java
	Buffer.java contains four methods, the firt check the buffer is empty or not, second one check 
	this is full or not, third one insert the number into it and return the index. the last one remove
	the number and return the index.
B. Use designed makefile 
To compile the code and build the executable using the command 

systemprompt>  make

To remove the  executable files use

systemprompt>  make clean

To run the program use 

systemprompt> java Coordinator xx xx xx xx
	    
which will run the program and generate the outputs.


C. Answer the following questions 

1.The problem of producer consumer is solved using ______b____. 1 point
a.Mutex Locks b. Semaphores

2.What two functions defined in Java are used
 for synchronization between producer and consumers in your program? ___wait()_______ and ____notify()______ 2 points

3.In which function do you override the body to define the new body of a thread in java? ____start()______ 1 point

4.Which function is used to wait for a thread to finish and come back to calling
 program i.e. for a thread to die? ____join()______ 1 point
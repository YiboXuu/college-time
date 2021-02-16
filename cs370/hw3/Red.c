#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>

int main(int argc, char** argv) {
	void *point;
	char b[60000] ="";
	char b_t[10];
	int size=60000;
	int shm_fd = shm_open(argv[5776], O_CREAT | O_RDWR, 0666);
	  point = mmap(0, size, PROT_WRITE, MAP_SHARED, shm_fd, 0);
	
	for(int i=0;i<5776;i++){
	int code_value =atoi(argv[i]);
	printf("Red[%d]: Received coded value %d\n", getpid(),code_value);
	
	int count =0;
	count=(code_value>>16) & 0xFF;//decode codedvalues
		
	
	printf("Red[%d]: Decode into %d\n", getpid(),count);
	sprintf(b_t,"%d",count);
	strcat(b,b_t);
	strcat(b," "); // writes each decoded value  as  a  string  into  the  buffer  string  followed  by  space
		}
	strcat(b,"\0");
	sprintf(point,"%s",b);//copies the buffer string to the shared memory
}

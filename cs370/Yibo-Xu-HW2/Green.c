#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	int code_value =atoi(argv[1]);
	printf("Green[%d]: Received coded value %d\n", getpid(),code_value);
	int count=0;
	
	count =(code_value >> 8) & 0xFF;
		
	
	printf("Green[%d]: Decode into %d\n", getpid(),count);
	

	
	

	 return count;
}

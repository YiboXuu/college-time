#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


int main(int argc, char** argv) {
	int code_value =atoi(argv[1]);
	printf("Blue[%d]: Received coded value %d\n", getpid(),code_value);
	int count=0;
	
	count = (code_value) & 0xFF;
		
	
	printf("Blue[%d]: Decode into %d \n", getpid(),count );
	


	

return count;
}

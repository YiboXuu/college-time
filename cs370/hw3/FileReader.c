#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdbool.h>
#define IMAGE_HEIGHT 76
#define IMAGE_WIDTH 76

int main(int argc, char **argv)
{	char* filename = "coded_image_1.txt";
	if (argc > 1)
		filename = argv[1];
		
	bool t =true;
    FILE* fp;
	fp = fopen(filename,"r");
	
	int count =atoi(argv[2]);
	char add[800];
	char results[60000]; 
	while(t){
		if(fgets(add,800,fp)==NULL)
			break;
		strcat(results,add);
		if(results[strlen(results)-1]=='\n')
			results[strlen(results)-1]=' ';     //all  5776  values  in  a  single  line, separated by spaces
		else
			results[strlen(results)-1]='\0';
		}
	fclose(fp);
	write(count,results,strlen(results));    //writes  the  text  to  the  pipe
	close(count);        //close 
	
    return 0;
}

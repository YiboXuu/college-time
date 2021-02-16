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
#define IMAGE_HEIGHT 76
#define IMAGE_WIDTH 76

int main(int argc, char *argv[])
{	char* filename = "coded_image_1.txt";
	if (argc > 1)
		filename = argv[1];

	if (argc <1)
		{
		fprintf(stderr,"Incorrect number of arguments");
		return 1;}
		

	char *coded_values[5778];
	char b[60000] = "";

	int array[2];
	pipe(array); //creates a pipe
	if(pipe(array) == -1){
	  	fprintf(stderr,"Could not create pipe.\n");    // checks if pipe creation failed
        exit(1);
	}

	int r = fork(); //forks a child process to execute FileReader
	if(r < 0){
        printf("Failed to fork!\n");
        return -1;
    }

	else if(r > 0){
			int waitstatus_v;
			wait(&waitstatus_v);
			
			close(array[1]);
        	read(array[0], b, sizeof(b));   // reads the contents then close the read end
        	close(array[0]);
	}else{	
			close(array[0]);
			char buffer[200];
			sprintf(buffer,"%d",array[1]);
        	execlp("./FileReader", "FileReader",filename,buffer, NULL);
        }
   
    
    
    const char space[2] =" ";
	coded_values[0] =strtok(b,space);

   for(int i=1;i<5776;i++){
	   coded_values[i] =strtok(NULL,space);       //separates the each coded value and stores individual values in the array coded_values[].
	   }

    int *childProcessID =(int *)malloc(sizeof(int)*3);
    void **point =(void**)malloc(sizeof(void*)*3);
    const char  shmPrefix[15] = "Shared_mem";
    char shmActualName[30];
    int red[IMAGE_HEIGHT*IMAGE_WIDTH], green[IMAGE_HEIGHT*IMAGE_WIDTH],blue[IMAGE_HEIGHT*IMAGE_WIDTH];	
    
  
    for(int i = 0; i < 3; i++){ //  //creates three shared memory segments
        childProcessID[i] = fork();
        
        strcpy(shmActualName,shmPrefix);
        if(i==0)
				strcat(shmActualName,"_red");
		else if(i==1)
				strcat(shmActualName,"_green");        //appropriate name       
		else
				strcat(shmActualName,"_blue");
				
		
		coded_values[5776] = shmActualName;             //name is written into the second last position in the array coded_value[5778]
		coded_values[5777] = NULL;
		/*for(int z = 0; z < 5778; z++)
			printf("-%s-\n",coded_values[z]);
		fflush(stdout);*/
        	
				
			
        if( childProcessID[i]  < 0){
        	printf("failed\n");
            return -1;
        }
        else if( childProcessID[i]  == 0){
			if(i==0)
					execvp("./Red", coded_values);                     //forks Red/Green/Blueprogram as a child process
			else if (i==1)
					execvp("./Green", coded_values);      
			else
					execvp("./Blue", coded_values);
        }		
        else{
            int shm_fd, size = 60000;                                                  
    
            shm_fd = shm_open(shmActualName, O_CREAT | O_RDWR, 0666);                //t prints the name and the file descriptor of the shared memory
            ftruncate(shm_fd, size);
            point[i] = (int *)mmap(0, size, PROT_READ, MAP_SHARED, shm_fd, 0);     
    
         /* int waitstatus_v;
            wait(&waitstatus_v);
            sscanf(*point, "%l[^\t\n]", &childProcessID[i]);
            shm_unlink(shmActualName);
            WEXITSTATUS(waitstatus_v);*/
        }
    }
          
          
   for(int i=0;i<3;i++){  //copies the values from the shared memory into the appropriate integer arrays of size  5776
			   
			int waitstatus_v;
			waitpid(childProcessID[i],&waitstatus_v,WCONTINUED);
			
			char b[60000];
			sscanf(point[i],"%[^\t\n]",b);
					
				
			if(i==0){
					 for(int j=0;j<5776;j++){
						 //printf("Test line\n");
			//fflush(stdout);	
						 if(j==0)
								red[j] = atoi(strtok(b," "));
							else
								 red[j] =atoi(strtok(NULL," "));
								 
							  }
							  
			}
			else if(i==1){
						
					 for(int j=0;j<5776;j++){
							if(j==0)
								green[j] = atoi(strtok(b," "));
							else
								 green[j] =atoi(strtok(NULL," "));
								 
							  }	  
			}
			else{
					 for(int j=0;j<5776;j++){
						 if(j==0)
								blue[j] = atoi(strtok(b," "));
						 else
								blue[j] =atoi(strtok(NULL," "));
								 
							  }
			}
			
			
			
			strcpy(shmActualName,shmPrefix);
			if(i==0)
				strcat(shmActualName,"_red");
			else if(i==1)
				strcat(shmActualName,"_green");
			else
				strcat(shmActualName,"_blue");
				
			shm_unlink(shmActualName);	 //unlinks  the  shared  memory
	}
					 
	
		char outputFileName[30]= "";
		char extension[12] = "_output.ppm";
		strcpy(outputFileName, filename);
		char* pos = strchr(outputFileName, '.');
		*pos = '\0';
		strcat(outputFileName, extension);	 
		FILE *fout = fopen(outputFileName, "wb");
		fprintf(fout, "P6\n%i %i 255\n", IMAGE_HEIGHT, IMAGE_WIDTH);         //creates the imagefile
		for (int i = 0; i < IMAGE_HEIGHT*IMAGE_WIDTH; i++)
			{
			fputc(red[i], fout); 
			fputc(green[i], fout); 
			fputc(blue[i], fout); 
				}
		fclose(fout);
		   
			   
        printf("Starter: %s file written and closed.\n",outputFileName);    
        
        
       return 0;

    
}

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#define IMAGE_HEIGHT 76
#define IMAGE_WIDTH 76

int main(int argc, char *argv[])
{	char* filename = "coded_image_1.txt";
	if (argc > 1)
		filename = argv[1];
	FILE* fp;
	fp = fopen(filename,"r");
	char outputFileName[30]= "";
	char extension[12] = "_output.ppm";
	strcpy(outputFileName, filename);
	char* pos = strchr(outputFileName, '.');
	*pos = '\0';
	strcat(outputFileName, extension);
	char coded_values[5776][10];
	for(int i=0;i<IMAGE_HEIGHT*IMAGE_WIDTH;i++){ 
		fscanf(fp,"%s",coded_values[i]);
	}
				

	int RED_VALUE[IMAGE_HEIGHT*IMAGE_WIDTH], GREEN_VALUE[IMAGE_HEIGHT*IMAGE_WIDTH], BLUE_VALUE[IMAGE_HEIGHT*IMAGE_WIDTH];
	for(int i=0;i<76*76;i++){
	 for(int j = 0; j < 3; j++) {
            pid_t child = fork();
            if(child == 0) {
                switch(j) {
                    case 0:
                        execlp("./Red", "Red",coded_values[i], NULL);
                        break;
                    case 1:
                       execlp("./Blue","Blue", coded_values[i], NULL);
                       break;
                    case 2:
						execlp("./Green","Green" , coded_values[i], NULL);
                        break;
                    default:
                        break;
                }
            }
            else if(child > 0) {
                int stat;
                printf("Starter: Forked process with ID %d.\n", child);
                printf("Starter: Waiting for process [%d].\n", child);
                wait(&stat);
                int stat2 = WEXITSTATUS(stat);

                switch(j) {
                    case 0:
                        RED_VALUE[i] =stat2;
                        break;
                    case 1:
                        BLUE_VALUE[i] = stat2;
                        break;
                     case 2:
                        GREEN_VALUE[i] = stat2;
                        break;
                    default:
                        break;
                }
                printf("Starter: Child process %d returned %d.\n", child, stat2);
            }
            else {
                fprintf(stderr, "Process Failed\n");
                return -1;
            }
        }
        
        
         /*while(!feof(fp1)){
        char  ch = fgetc(fp1);
        //printf("%c",ch);
        if(ch == '\n'){
            number_of_pross++;
            //printf("%d",number_of_pross);
        }
    }*/

    //Process Processes[number_of_pross];
   /* Processes[1].Process_ID =3;
    Processes[1].Arrival_Time =0;
    Processes[1].Burst_Duration =3;
    Processes[1].Priority =2;
    Processes[0].Process_ID =2;
    Processes[0].Arrival_Time =0;
    Processes[0].Burst_Duration =5;
    Processes[0].Priority =4;
    Processes[2].Process_ID =1;
    Processes[2].Arrival_Time =9;
    Processes[2].Burst_Duration =8;
    Processes[2].Priority =1;
    Processes[3].Process_ID =4;
    Processes[3].Arrival_Time =10;
    Processes[3].Burst_Duration =6;
    Processes[3].Priority =3;*/
    //number_of_pross=0;
//Processes[1].Process_ID =12;
	
   /* while( fscanf(fp1, "%d,%d,%d,%d",&Processes[number_of_pross].Process_ID,&Processes[number_of_pross].Arrival_Time,&Processes[number_of_pross].Burst_Duration,&Processes[number_of_pross].Priority)!= EOF	){
        number_of_pross++;
       // printf("%d",number_of_pross);
    }*/
	}
        
    	FILE *fout = fopen(outputFileName, "wb");
		fprintf(fout, "P6\n%i %i 255\n", IMAGE_HEIGHT, IMAGE_WIDTH);
		for (int i = 0; i < IMAGE_HEIGHT*IMAGE_WIDTH; i++)
			{
			fputc(RED_VALUE[i], fout); // 0 .. 255
			fputc(GREEN_VALUE[i], fout); // 0 .. 255
			fputc(BLUE_VALUE[i], fout); // 0 .. 255
				}
		fclose(fout);
        
     printf("Starter: %s file written and closed.\n",filename);        
       return 0;

    
}

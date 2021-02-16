#include<stdio.h> 
#include<string.h>
#include<ctype.h>
#include <stdlib.h>


typedef struct{
    int Process_ID;
    int Arrival_Time;
    int Burst_Duration;
    int Priority;
    int TurnAroundTime;
    int WaitTime;
    int remain_Time;
    int fp;
}Process;


typedef struct{
  int Process_ID;
  int Arrival_Time;
  int End_Time;
}Gantt;

typedef struct{
  int idle_Start;
  int idle_End;
}IDLE;


void FCFS(Process Processes[], int number);
void PBS(Process Processes[], int number);
void RR(Process Processes[],int number,int time);
void print_table (Process process[],int number,char* name);
void print_Gantt(Gantt gantt[],int n, char* filename,IDLE idle[]);

int main(int argc,char **argv) {
   FILE *fp1;
   char* file_name = argv[1];
   fp1=fopen(file_name,"r"); //opening the file
    	if (argc != 3){
       		printf("Incorrect number of arguments.\n");
       	 	return -1;
    	}
    int quantum_time;
    quantum_time = atoi(argv[2]);
	//printf("%d",quantum_time);
	int number_of_pross = 0;
    while(!feof(fp1)){
        char  ch = fgetc(fp1);
       // printf("%c",ch);
        if(ch == '\n'){
            number_of_pross++;
            //printf("%d",number_of_pross);
        }
    }

    Process Processes[number_of_pross];
    fseek(fp1, 0, SEEK_SET);
    number_of_pross=0;
	char buffer[100];
	fgets(buffer,100,fp1);
    while( fscanf(fp1,"%d,%d,%d,%d",
    &Processes[number_of_pross].Process_ID,
    &Processes[number_of_pross].Arrival_Time,
    &Processes[number_of_pross].Burst_Duration,
    &Processes[number_of_pross].Priority)!= EOF	){
        number_of_pross++;
       // printf("pross number is %d",number_of_pross);
    }


    fclose(fp1);

    FCFS(Processes,number_of_pross);
	PBS( Processes, number_of_pross);
	RR(  Processes, number_of_pross,quantum_time);
    return 0;

}

void RR(Process Processes[], int number,int quantum_time){

for(int i = 1; i < number; i++) {
		for(int j = 0; j < number-i; j++) {
		if(Processes[j].Process_ID > Processes[j+1].Process_ID){
			Process temp = Processes[j];
	            Processes[j] = Processes[j+1];
	            Processes[j+1] = temp;
		
		}
		
}}

double totalW =0;
double totalT =0;
 Process RRQueue[number];
	for (int i = 0; i < number; i++) { 
		RRQueue[i] = Processes[i];
		//printf("%d",RRQueue[i].Arrival_Time);
	}

for(int i = 1; i < number; i++) {  //sort by arrival time
		for(int j = 0; j < number-i; j++) {
		
	    	if(RRQueue[j].Arrival_Time > RRQueue[j+1].Arrival_Time) {
	        	 Process temp = RRQueue[j];
	            RRQueue[j] = RRQueue[j+1];
	            RRQueue[j+1] = temp;  
	         }	
	        if (RRQueue[j].Arrival_Time == RRQueue[j+1].Arrival_Time) {
				 //sort by process IDs if same arrival
				 if (RRQueue[j].Process_ID > RRQueue[j+1].Process_ID) {
	 	        	 Process temp = RRQueue[j];
	          		  RRQueue[j] = RRQueue[j+1];
	           		  RRQueue[j+1] = temp;}
			 }
	 }
}
//printf("stop here");
//int ft[10];
for(int i=0;i<number;i++){
	//printf("%d",RRQueue[i].Process_ID);
	RRQueue[i].remain_Time = RRQueue[i].Burst_Duration;
	//ft[i] =0;
}

Gantt RRGantt[10];
//int zero = 0;
IDLE idle[10];
int runCount = 0;
int flag = 0;
int count =number;
int i=0;
int ganttCount=0;
//printf("stop here");
	while(count != 0) {
		//printf("stop here");
		RRGantt[ganttCount].Process_ID = RRQueue[i].Process_ID;
		//printf("process id is %d ",RRGantt[ganttCount].Process_ID);
		//printf("runCount is  %d \n",runCount);
		//printf("process id is %d \n",RRQueue[i].Process_ID);
		RRGantt[ganttCount].Arrival_Time = runCount;
		
		if(RRQueue[i].remain_Time>0){
			if(RRQueue[i].remain_Time <= quantum_time &&  RRQueue[i].remain_Time >0){
				runCount +=  RRQueue[i].remain_Time;
				RRQueue[i].remain_Time =0;
				flag =1;
			}else{
				runCount += quantum_time;
				RRQueue[i].remain_Time -= quantum_time;
				
			}
		RRGantt[ganttCount].End_Time = runCount;
		//i++;
		}
		//printf("runCount is  %d \n",runCount);
		if(RRQueue[i].remain_Time ==0&& flag ==1){
			RRQueue[i].fp = runCount;
			flag=0;
			count--;
		}
		
		if(RRQueue[i-1].remain_Time >0 && i!=0 ){
				i--;
			}else{
				i++;
			}
		
		if(RRQueue[i-1].remain_Time == 0 && RRQueue[i].remain_Time ==0){
				i++;
		}
		int zero =0;
		//printf("%d arrival time is %d \n",RRQueue[i].Process_ID,RRQueue[i].Arrival_Time);
		if(runCount < RRQueue[i].Arrival_Time){
			//printf("%d arrival time is %d \n",RRQueue[i].Process_ID,RRQueue[i].Arrival_Time);
					idle[zero].idle_Start = runCount;
					runCount  = RRQueue[i].Arrival_Time;
					//RRGantt[ganttCount].Arrival_Time  =runCount;
					idle[zero].idle_End = runCount;
			}
		
		ganttCount++;
	}
	//printf("%d process id is. \n",RRGantt[0].Process_ID);
	for(int i = 1; i < number; i++) { //make temp process follow by id
		for(int j = 0; j < number-i; j++) {
		if(RRQueue[j].Process_ID > RRQueue[j+1].Process_ID){
			 Process temp = RRQueue[j];
	 	            RRQueue[j] = RRQueue[j+1];
	 	            RRQueue[j+1] = temp;
		}
	}}
	
	
	
	//Processes[0].WaitTime = 0; //first process doesn't wait 
	for (int i = 0; i < number; i++) {
		Processes[i].WaitTime = RRQueue[i].fp - RRQueue[i].Arrival_Time- RRQueue[i].Burst_Duration;
		totalW += Processes[i].WaitTime;
	}
	
	
	for (int i = 0; i < number; i++) {
		Processes[i].TurnAroundTime = RRQueue[i].fp - RRQueue[i].Arrival_Time;
		totalT += Processes[i].TurnAroundTime;
	}
//int j=0;
   
	char RR[] = "Round Robin";
	print_table(Processes,number,RR);
	print_Gantt(RRGantt, ganttCount, RR,idle);
		//printf("%d\n",quantum_time);
		
	double totalProcess = (double)number;
	double endTime = (double)runCount;
	
	printf("Average Waiting Time: %.1f\n", totalW/number);
	printf("Average Turnaround Time: %.1f\n", totalT/number);
	printf("Throughput: %.12f\n", totalProcess/endTime);
	printf("\n");

}


void FCFS(Process Processes[], int number){

for(int i = 1; i < number; i++) {
		for(int j = 0; j < number-i; j++) {
		if(Processes[j].Process_ID > Processes[j+1].Process_ID){
			Process temp = Processes[j];
	            Processes[j] = Processes[j+1];
	            Processes[j+1] = temp;
		
		}
}}

double totalW =0;
double totalT =0;
 Process FCFSQueue[number];
	for (int i = 0; i < number; i++) {
		FCFSQueue[i] = Processes[i];
		//printf("%d",FCFSQueue[i].Arrival_Time);
	}
	
	for(int i = 1; i < number; i++) {
		for(int j = 0; j < number-i; j++) {
	    	if(FCFSQueue[j].Arrival_Time > FCFSQueue[j+1].Arrival_Time) {
	        	 Process temp = FCFSQueue[j];
	            FCFSQueue[j] = FCFSQueue[j+1];
	            FCFSQueue[j+1] = temp;
	            
	            //printf("%d",FCFSQueue[j].Process_ID);
	         }
			 if (FCFSQueue[j].Arrival_Time == FCFSQueue[j+1].Arrival_Time) {
				 //sort by process IDs if same arrival
				 if (FCFSQueue[j].Process_ID > FCFSQueue[j+1].Process_ID) {
	 	        	 Process temp = FCFSQueue[j];
	 	            FCFSQueue[j] = FCFSQueue[j+1];
	 	            FCFSQueue[j+1] = temp;
	 	            
	 	            //printf("%d",FCFSQueue[j].Process_ID);
				 }
			 }
	    }
	}
	
	IDLE  idle[0];
	
	Gantt FCFSGantt[number];
	int runCount = 0;
	for(int i = 0; i < number; i++) {
		FCFSGantt[i].Process_ID = FCFSQueue[i].Process_ID;
		FCFSGantt[i].Arrival_Time = runCount;
			if(runCount < FCFSQueue[i].Arrival_Time ){
					idle[0].idle_Start = runCount;
					//id = FCFSQueue[i].Arrival_Time - runCount;
					runCount  = FCFSQueue[i].Arrival_Time;
					FCFSGantt[i].Arrival_Time  =runCount;
					idle[0].idle_End = runCount;
			}
		//printf("%d now time is  %d\n",FCFSGantt[i].Process_ID,FCFSGantt[i].Arrival_Time);
		runCount += FCFSQueue[i].Burst_Duration;
		FCFSGantt[i].End_Time = runCount;
	}
	
	Gantt tempQueue[number];
	for (int i = 0; i < number; i++) {
		tempQueue[i] = FCFSGantt[i];
		//printf("%d",FCFSQueue[i].Arrival_Time);
	} 
	for(int i = 1; i < number; i++) { //make temp process follow by id
		for(int j = 0; j < number-i; j++) {
		if(FCFSQueue[j].Process_ID > FCFSQueue[j+1].Process_ID){
			 Process temp = FCFSQueue[j];
	 	            FCFSQueue[j] = FCFSQueue[j+1];
	 	            FCFSQueue[j+1] = temp;
		}
		if(tempQueue[j].Process_ID > tempQueue[j+1].Process_ID){
			 Gantt temp = tempQueue[j];
	 	           tempQueue[j] = tempQueue[j+1];
	 	            tempQueue[j+1] = temp;
		}
	}}
	
	//waittime;
	Processes[0].WaitTime = 0; //first process doesn't wait 
	for (int i = 1; i < number; i++) {
		//printf("%d ",FCFSGantt[i].Arrival_Time);
		//printf("%d ",FCFSQueue[i].Arrival_Time);
		Processes[i].WaitTime = tempQueue[i].Arrival_Time - FCFSQueue[i].Arrival_Time;
		totalW += Processes[i].WaitTime;
	}
	
	//TurnAroundTime
	for (int i = 0; i < number; i++) {
		Processes[i].TurnAroundTime = Processes[i].WaitTime + Processes[i].Burst_Duration;
		totalT += Processes[i].TurnAroundTime;
	}

	char FCFS[] = "FCFS";
	print_table(Processes,number,FCFS);
	print_Gantt(FCFSGantt, number, FCFS,idle);
	
	double totalProcess = (double)number;
	double endTime = (double)runCount;
	printf("Average Waiting Time: %.1f\n", totalW/number);
	printf("Average Turnaround Time: %.1f\n", totalT/number);
	printf("Throughput: %.12f\n", totalProcess/endTime);
	printf("\n");
}


void PBS(Process Processes[], int number){

for(int i = 1; i < number; i++) {
		for(int j = 0; j < number-i; j++) {
		if(Processes[j].Process_ID > Processes[j+1].Process_ID){
			Process temp = Processes[j];
	            Processes[j] = Processes[j+1];
	            Processes[j+1] = temp;
		
		}
}}

	double totalW =0;
	double totalT =0;
 	Process PBSQueue[number];
	for (int i = 0; i < number; i++) {
		PBSQueue[i] = Processes[i];
		//printf("%d",FCFSQueue[i].Arrival_Time);
	}
	int burst=0;
	for(int i = 1; i < number; i++) {
		for(int j = 0; j < number-i; j++) {
	    	/*if(PBSQueue[j].Priority > PBSQueue[j+1].Priority) {
	        	Process temp = PBSQueue[j];
	            PBSQueue[j] = PBSQueue[j+1];
	            PBSQueue[j+1] = temp;   
	            //printf("%d",FCFSQueue[j].Process_ID);
	         }*/
			
	         //printf("%d",PBSQueue[j].Process_ID);	
	         if(PBSQueue[j].Arrival_Time > PBSQueue[j+1].Arrival_Time){
	         Process temp = PBSQueue[j];
	            PBSQueue[j] = PBSQueue[j+1];
	            PBSQueue[j+1] = temp;
	            //printf("%d",FCFSQueue[j].Process_ID);
	         }
	         if (PBSQueue[j].Arrival_Time == PBSQueue[j+1].Arrival_Time) {
				 //sort by process IDs if same arrival
				 if (PBSQueue[j].Priority > PBSQueue[j+1].Priority) {
	 	        	 Process temp = PBSQueue[j];
	 	            PBSQueue[j] = PBSQueue[j+1];
	 	            PBSQueue[j+1] = temp;          
	 	            //printf("%d \n",PBSQueue[j].Process_ID);
				 }
			 } 
			}
			 
	    }
	   
	int x =1; 
	for(int i=0;i<number;i++){
		burst += PBSQueue[i].Burst_Duration;
		for(int i=x; i<number;i++){
			if(burst >= PBSQueue[i].Arrival_Time ){
				if(PBSQueue[x].Priority > PBSQueue[i].Priority){
						printf("%d \n",PBSQueue[i].Process_ID);
				 	Process temp = PBSQueue[x];
	 	            PBSQueue[x] = PBSQueue[i];
	 	            PBSQueue[i] = temp;
				}
		}
		}
		x++;
	
	}
	//printf("%d \n",PBSQueue[2].Process_ID);
	
	IDLE  idle[0];
	
	Gantt PBSGantt[number];
	int runCount = 0;
	for(int i = 0; i < number; i++) {
	 //printf("%d",PBSQueue[i].Process_ID);
		PBSGantt[i].Process_ID = PBSQueue[i].Process_ID;
		PBSGantt[i].Arrival_Time = runCount;
			if(runCount < PBSQueue[i].Arrival_Time ){
					idle[0].idle_Start = runCount;
					//id = FCFSQueue[i].Arrival_Time - runCount;
					runCount  = PBSQueue[i].Arrival_Time;
					PBSGantt[i].Arrival_Time  =runCount;
					idle[0].idle_End = runCount;
			}
		//printf("%d now time is  %d\n",FCFSGantt[i].Process_ID,FCFSGantt[i].Arrival_Time);
		runCount += PBSQueue[i].Burst_Duration;
		PBSGantt[i].End_Time = runCount;
	}
	
	Gantt tempQueue[number];
	for (int i = 0; i < number; i++) {
		tempQueue[i] = PBSGantt[i];
		//printf("%d",FCFSQueue[i].Arrival_Time);
	} 
	
	for(int i = 1; i < number; i++) { //make temp process follow by id
		for(int j = 0; j < number-i; j++) {
		if(PBSQueue[j].Process_ID > PBSQueue[j+1].Process_ID){
			 Process temp = PBSQueue[j];
	 	            PBSQueue[j] = PBSQueue[j+1];
	 	            PBSQueue[j+1] = temp;
		}
		if(tempQueue[j].Process_ID > tempQueue[j+1].Process_ID){
			 Gantt temp = tempQueue[j];
	 	            tempQueue[j] = tempQueue[j+1];
	 	            tempQueue[j+1] = temp;
		}
	}}
	
	//WaitTime
	Processes[0].WaitTime = 0; //first process doesn't wait 
	for (int i = 1; i < number; i++) {
		//printf("%d ",FCFSGantt[i].Arrival_Time);
		//printf("%d ",FCFSQueue[i].Arrival_Time);
		Processes[i].WaitTime = tempQueue[i].Arrival_Time - PBSQueue[i].Arrival_Time;
		totalW += Processes[i].WaitTime;
	}
	
	//TurnAroundTime
	for (int i = 0; i < number; i++) {
		Processes[i].TurnAroundTime = Processes[i].WaitTime + Processes[i].Burst_Duration;
		totalT += Processes[i].TurnAroundTime;
	}

	char PBS[] = "PBS";
	print_table(Processes,number,PBS);
	print_Gantt(PBSGantt, number, PBS,idle);
	
	double totalProcess = (double)number;
	double endTime = (double)runCount;
	
	
	printf("Average Waiting Time: %.1f\n", totalW/number);
	printf("Average Turnaround Time: %.1f\n", totalT/number);
	printf("Throughput: %.12f\n", totalProcess/endTime);
	printf("\n");
}



void print_table(Process p[],int n, char* filename){
int i;
printf("----------------- %2s -----------------\n",filename);
puts("Process ID  | Waiting Time  | Turnaround Time ");
for(i=0;i<n;i++){
printf("     %-2d     |      %-2d       |        %-2d      \n",
	p[i].Process_ID,p[i].WaitTime,p[i].TurnAroundTime);
}
printf("\n");
}


void print_Gantt(Gantt g[],int n, char* filename,IDLE idle[]){

		printf("Gantt Chart is:\n");
		for(int i=0;i<n;i++){
			printf("[  %-2d  ]--  %d   --[  %-2d  ]\n",
			g[i].Arrival_Time ,g[i].Process_ID,g[i].End_Time);
				
			if(idle[0].idle_Start == g[i].End_Time ){
					printf("[  %-2d  ]-- IDLE --[  %-2d  ]\n", 
					idle[0].idle_Start ,idle[0].idle_End);
			}
		
	}
	printf("\n");
}


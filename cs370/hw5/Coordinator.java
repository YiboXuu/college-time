import java.lang.Exception;
import java.time.Instant;
import java.time.Clock;
import java.time.Duration;

class Coordinator 
{
	public static void main(String[] args) throws InterruptedException 
	{		int checkSum = 0,cCheckSum=0;
			int bufferSize=0,number=0,seed=0,ID=0,id = 0;
		if(args.length<3){return;}
					try{ 
							bufferSize = Integer.parseInt(args[0]);
							number = Integer.parseInt(args[1]);
							ID = Integer.parseInt(args[2]);
							seed = Integer.parseInt(args[3]);
	if(number<0 || bufferSize<0 || seed<0 || ID< 0 ){return;}
	}catch(Exception e){return;}
	        //producer
					Buffer buffer = new Buffer(bufferSize);
					
					// create and run producers and consumers
					Producer producer1 = new Producer(buffer, number, seed);
					producer1.start();
					
					int x= (number/ID);
					Consumer[] consumer1 = new Consumer[ID];
					for(int i=0;i<ID;i++) {
						consumer1[i]= new Consumer(buffer,x,i+1);
						
						consumer1[i].start();
					}
					
					
					for(int i=0;i<ID;i++) {
						try {
							consumer1[i].join();
							cCheckSum += consumer1[i].getChecksum();
						} catch (InterruptedException e) {
							System.out.println(e);
						}
					}
					checkSum = producer1.getChecksum();
			System.out.println();
	        System.out.printf("Producer : Finished producing %d items with checksum being %d \n",number,checkSum);
	        System.out.println();
	        System.out.printf("\033[0;4mConsumers: Finished consuming %d items with checksum being %d\033[0;0m \n", number,cCheckSum);
			//System.out.println();
	}


	public static String getTime()
	{
		Clock offsetClock = Clock.offset(Clock.systemUTC(), Duration.ofHours(-9));
		Instant time = Instant.now(offsetClock);
		String timeString = time.toString();
		timeString = timeString.replace('T', ' ');
		timeString = timeString.replace('Z', ' ');
		return(timeString);
	}
}

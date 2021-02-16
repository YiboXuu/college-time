
import java.util.Random;

public class Producer extends java.lang.Thread  
{
	//Necessary variables and object declaration
	Random randomWithSeed;
	Coordinator coo;
	Buffer buff;
	int count,c=0;
	int checkSum = 0;
	public Producer(Buffer buff, int count,int seed) 
	{	this.buff = buff;
		this.count = count;
		randomWithSeed = new Random(seed);
	}
	
	public int getChecksum() {
		return this.checkSum;
	}
	
	public synchronized void produce() {
		
		
		if(!buff.isFull()) {
			//buff.insert(variable);
			
			int variable = randomWithSeed.nextInt(100);
			checkSum += variable; 
			try {
				System.out.println("Producer     inserted " + variable + "  at  index " + buff.insert(variable) + " at time "+ coo.getTime());
				System.out.flush();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			buff.notifyAll();
			c++;
			
		}else {
			try {
                buff.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
		}
}
		
		
		
	
	@Override
	public void run() 
	{ //int variable = randomWithSeed.nextInt(99);
	
	 while (c < count) {
		 //System.out.println(c);
         synchronized(buff){produce();}
         
     	}
			}
    
	
}

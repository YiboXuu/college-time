import java.util.Random;

public class Consumer extends java.lang.Thread {
	Buffer buff;
	Coordinator coo;
	Random randomWithSeed;
	    int checkSum,c = 0, count;
	     int id;

	    public Consumer(Buffer buff, int count,int ID) 
		{	this.buff = buff;
			this.count = count;
			this.id = ID;
		}

	    public int getID() {
	        return this.id;
	    }
	    
	    public int getChecksum() {
			return this.checkSum;
		}
	    
	    public synchronized void consume() throws InterruptedException{
			if(!buff.isEmpty()) {
				int x = buff.getRemove();
				checkSum += x; 
				try {
					System.out.printf("\033[0;4mConsumer %3d consumed %d from index %d at time \033[0;0m",id,x,buff.remove());
					System.out.print(Coordinator.getTime()  + "\n");
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


	    public void run() {
	        while(c < count){
				
	        	synchronized(buff){
				try {
	                consume();
	            } catch (InterruptedException e) {
	                e.printStackTrace();
	            }
					
					}
	        	
	           	}
	    
	    }

}

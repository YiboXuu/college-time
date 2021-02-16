public class Buffer {
	int[] buffer;
	int in,out,size,len,place;
	
	public Buffer(int buf_size){
		this.size = buf_size;
		buffer = new int[size];
		in = out = len = 0;
	}
	
	boolean isEmpty(){return len == 0;}
	
	boolean isFull(){return len == size;}
	
	public synchronized int insert(int item) throws InterruptedException{
		    int place = in;
		    buffer[in] = item;
		    len++;
		    in = (in+1) % size;
		    return place;
		   }

	public synchronized int remove()  throws InterruptedException{ 
		    int place = out;
		     len--;
		     out = (out+1) % size;
		     return place;
		   }
		   
		   
	public synchronized int getRemove()  throws InterruptedException{ 
			return buffer[out];	
		}
}


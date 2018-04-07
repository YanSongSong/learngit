package junkCode;

public class InstanceCounter {
	private static int num=0;
	protected static int getCounter() {
		return num;
	}
	private static void addInstance() {
		num++;
	}
	InstanceCounter(){
		InstanceCounter.addInstance();
	}
	public static void main(String[] arguments) {
		System.out.println("Starting with "+getCounter()+" instances");
		for(int i=0;i<500;++i) {
			new InstanceCounter();
		}
		System.out.println("created "+InstanceCounter.getCounter()+" instances");
	}
}

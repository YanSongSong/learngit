package junkCode;

public class ChangeType {
	public static void main(String[] args) {
		float a=100.98f;
		Float F1=new Float(a);
		double b=F1.doubleValue();		
		System.out.println("b="+b);//上面的是float转double
		int s=2;
		Long s1=new Long(s);
		long d=s1.longValue();
		System.out.println("d="+d);//上面的是int转long
	}
}

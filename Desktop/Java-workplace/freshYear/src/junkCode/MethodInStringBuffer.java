package junkCode;

public class MethodInStringBuffer {
	public static void main(String args[]) {
		StringBuffer b=new StringBuffer("HDZTXDY");
		StringBuffer b1=new StringBuffer();
		b.delete(2, 4);
		b1=b.reverse();
		System.out.print(b1);
		System.out.print(b);
	}
}

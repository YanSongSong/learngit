package junkCode;

public class MaxTest {
	public static int max(int m,int n) {
		if(m>n) {
			return m;
		}
		else {
			return n;
		}
	}
	public static void main(String[] args) {
		int x=9;
		int y=8;
		int maxNumber=max(x,y);
		System.out.println("The max number is:"+maxNumber);
	}
}

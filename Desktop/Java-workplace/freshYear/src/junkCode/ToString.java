package junkCode;

public class ToString {
	public static void main(String[] args) {
		int a=34;
		int b=12;
		int c=89;
		Integer X1=new Integer(a);
		Integer X2=new Integer(b);
		Integer X3=new Integer(c);
		X1.toString();//第一种搞法
		String.valueOf(X3);//第三种搞法
		System.out.println(X1+"yeee"+X2+""+X3);//第二种搞法
	}
}

package junkCode;
//接口的写法
public interface CalInterface{
	final static float PI=3.14159f;
	float getArea(float r);
	float getCircumStances(float r);
}
public class InterfaceUse implements CalInterface {
	public float getArea(float r) {
		return PI*r*r;
	}
	public float getCircumStances(float r) {
		return 2*PI*r;
	}
	public static void main(String []args) {
		InterfaceUse I=new InterfaceUse();
		System.out.println(I.getArea(2));
		System.out.println(I.getCircumStances(2));
	}
}

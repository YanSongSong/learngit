package junkCode;
class Vehicle{}
public class Car extends Vehicle{
	public static void main(String[] args) {
		Car a=new Car();
		Vehicle b=new Vehicle();
		boolean result1=a instanceof Car;
		boolean result2=a instanceof Vehicle;
		boolean result3=b instanceof Car;
		boolean result4=b instanceof Vehicle;
		System.out.println(result1);
		System.out.println(result2);
		System.out.println(result3);
		System.out.println(result4);
	}
}

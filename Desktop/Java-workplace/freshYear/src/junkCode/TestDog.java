package junkCode;

public class TestDog {
	public static void main(String[] args) {
		Mammal a=new Mammal("鸽子");
		a.SayHi();
		Mammal b=new Cat("猫");
		b.SayHi();
	}
	/*用Mammal b=new Cat("猫")时实际调用的是new后面关键字里的方法，
	 * 这样就可以解释为什么猫说了Hello
	 */
}
class Mammal{
	private String name;
	public Mammal(String name) {
		this.name=name;
		System.out.println("My name is:"+this.name);
	}
	public void SayHi(){
		System.out.println("Hi");
	}
}
class Cat extends Mammal{
	public Cat(String name) {
		super(name);
		System.out.println("WtyBill");
	}
	public void SayHi() {
		System.out.println("Hello");
	}
}
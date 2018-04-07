package junkCode;
public interface A{
	public void eat();
	public void sleep();
}
public interface B{
	public void show();
}
public class C implements A,B{
	public void eat() {
		System.out.println("你见过饭都吃不起的带明星吗？");
	}
	public void sleep() {
		System.out.println("那真的牛p");
	}
	public void show() { 
		System.out.println("你把你闪现给我交了");
	}
	public static void main(String[] args) {
		C mata=new C();
		mata.eat();
		mata.sleep();
		mata.show();
	}
}


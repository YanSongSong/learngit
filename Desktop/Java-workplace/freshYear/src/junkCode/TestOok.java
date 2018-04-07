package junkCode;

public class TestOok {
	public static void main(String[]args) {
		Ook a=new Ook("牛");
		a.SayHi();
	}
}
class Ook extends Mammal{
	public Ook(String name) {
		super(name);
		System.out.println("Mou~");
	}
}
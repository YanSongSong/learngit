package junkCode;

public class ConstructionMethod {
	public ConstructionMethod(String name) {
		System.out.println("The dog's name is:"+name);
	}
	public static void main(String[] args) {
		ConstructionMethod myFirstConstructionMethod=new ConstructionMethod("Tom");
	}
}

package junkCode;

public class Puppy {
	/*in this program we will use ConstructionMethod,
	 * and also,
	 * encapsulation
	 */
	int puppyAge;
	public Puppy(String name) {
		System.out.println("Puppy's name is:"+name);
	}
	public void setAge(int age) {
		puppyAge=age;
	}
	public int getAge() {
		System.out.println("Puppy's age is:"+puppyAge);
		return puppyAge;
	}
	public static void main(String[] args) {
		Puppy myPuppy=new Puppy("Tom");
		myPuppy.setAge(2);
		int v=myPuppy.getAge();
		System.out.println("The variable is:"+v);
	}
}

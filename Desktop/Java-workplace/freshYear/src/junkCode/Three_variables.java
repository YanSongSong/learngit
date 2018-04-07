package junkCode;

public class Three_variables {
	int age;
	static int salary=100;
	String name;//我偷个懒不写构造方法，好吧
	public void setAge(int a) {
		this.age=a;
	}
	public int getAge() {
		return this.age;
	}
	public void setName(String n) {
		this.name=n;
	}
	public String getName() {
		return this.name;
	}//封装完成
	public void printName() {
		System.out.println("The name is:"+this.name);
	}
	public void printAge() {
		System.out.println("The age is:"+this.age);
	}
	public void printSalary() {
		System.out.println("The salary is:"+salary);
	}
	public static void main(String[] args) {
		Three_variables v=new Three_variables();
		v.age=18;
		v.name="YanSongSong";
		v.printName();
		v.printAge();
		v.printSalary();
	}
}

package junkCode;

class Animal2 {
		private String name;  
	    private int id; 
	    public Animal2(String myName, int myid) { 
	        name = myName; 
	        id = myid;
	    } 
	    public void eat(){ 
	        System.out.println(name+"正在吃"); 
	    }
	    public void sleep(){
	        System.out.println(name+"正在睡");
	    }
	    public void introduction() { 
	        System.out.println("大家好！我是"+ id + "号" + name + "."); 
	    } 
}
class Penguin extends Animal2{
	public Penguin(String myName,int myid) {
		super(myName,myid);
	}
	void bark() {
		System.out.println("jiji");
	}
}
class Mouse extends Animal2{
	public Mouse(String myName,int myid) {
		super(myName,myid);
	}
	void bark() {
		System.out.println("zhizhi");
	}
}
public class Animal1{
	public static void main(String[] args) {
	Penguin a=new Penguin("ass",1);
	Mouse b=new Mouse("hole",2);
	a.eat();
	a.sleep();
	a.introduction();
	a.bark();
	b.eat();
	b.sleep();
	b.introduction();
	b.bark();
	/*这里如果用Animal1 a=new Penguin("ass",1)就不能调用bark方法，
	 * 因为在父类中没有bark方法
	 */
}
}

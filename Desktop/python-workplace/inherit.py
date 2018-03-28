#inherit
class schoolMember():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("'Initialized name :{}'".format(self.name))
    def tell(self):
        print("My name is {}. I'm now {} years old".format(self.name,self.age))
class student():
    def __init__(self,name,age,mark):
        schoolMember.__init__(self,name,age)
        self.mark=mark
    def tell(self):
        schoolMember.tell(self)
        print('Mark:{}'.format(self.mark))
class teacher():
    def __init__(self,name,age,salary):
        schoolMember.__init__(self,name,age)
        self.salary=salary
    def tell(self):
        schoolMember.tell(self)
        print('Salary:{}'.format(self.salary))
s=student('Tom',18,100)
t=teacher('Jerry',40,2000)
members=[s,t]
for member in members:
    member.tell()

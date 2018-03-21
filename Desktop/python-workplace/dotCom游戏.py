import random
class dotCom:
    def __name__(self,name):
        self.name=name;
    def __number__(self,number):
        self.number=number;
dotCom1=dotCom()
dotCom2=dotCom()
dotCom3=dotCom()
dotCom1.__name__('baidu')
dotCom1.__number__(random.randint(0,10))
dotCom2.__name__('google')
dotCom2.__number__(random.randint(0,10))
dotCom3.__name__('jingdong')
dotCom3.__number__(random.randint(0,10))
dotComList=[dotCom1,dotCom2,dotCom3]
n=0
while True:
    if (len(dotComList)!=0):
        n=n+1
        guess=int(input('please input a number range in 0 to 9:'))
        for i in range(0,len(dotComList)):
            if(guess==dotComList[i].number):
                print('hit',dotComList[i].name)
                if(len(dotComList)==3):
                    print('miss others')
                elif(len(dotComList)==2):
                    print('miss 另外一个')
                dotComList.remove(dotComList[i])
                break
            else:
                print("miss",dotComList[i].name)
    else:
        print('You win this stupid game in',n,'步')
        break
#为什么会发生数组越界的问题

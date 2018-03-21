class person:
    def nameSet(self,name):
        self.name=name;
    def hello(self):
        print(self.name+":hello!")
a=person()
a.nameSet("Nancy")
a.hello()
#在python里nameSet什么的似乎都被叫做__init__

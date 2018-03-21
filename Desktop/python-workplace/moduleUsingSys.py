import sys
import os
print("The System arguments are:")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is",sys.path,'\n')
print(os.getcwd())
#import sys:指示系统寻找sys模块，sys模块是系统内置的模块，系统会知道如何去寻找它
#否则系统将从提供的sys.path中去寻找
#找到模块后系统将对其初始化使其中的语句能够使用，初始化只用进行一次
#sys.argv包含了命令行参数列表，命令行参数用数组来保存
#可以通过import os和print(os,getcwd())来查看当前程序所在目录


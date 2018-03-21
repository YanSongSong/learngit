def printMax(x,y):
    '''This is a Docstring test program.

    Now we start from the third line'''
    if(x>y):
        print(x,'is bigger');
    elif(x==y):
        print(x,'is equal to',y)
    else:
        print(y,'is bigger')
printMax(32,3)
print(printMax.__doc__)
#只有写在第一行的才算是DocString
#如果除了第一行以外还想接着写的话，建议空掉第二行，然后第三行缩进4
#然后还要注意在用DocString的时候要两个下划线符

#从1加到100的递归写法
def recurrency(x,result):
    if(x==1):
        return result+1
    else:
        return recurrency(x-1,result+x)
print(recurrency(100,0))

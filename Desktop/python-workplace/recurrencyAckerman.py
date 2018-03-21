#阿克曼函数
m=int(input('输入m:'))
n=int(input('输入n:'))
def recurrencyAckerman(m,n):
    if m==0:
        return n+1
    if m>0 and n==0:
        return recurrencyAckerman(m-1,1)
    if m>0 and n>0:
        return recurrencyAckerman(m-1,recurrencyAckerman(m,n-1))
result=recurrencyAckerman(m,n)
print(result)

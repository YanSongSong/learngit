#This is my shopping list
mylist=['BX','OkidaSan','Lilth','Arthur']
print('I have',len(mylist),'kinds things')
print('They are',mylist)
mylist.sort()
print('sorted list is',mylist)
print('oh no,I forgot one item.')
mylist.append('WuZang')
print('ok,now my list is',mylist)  
for item in mylist:
    print('Now I wanna buy',mylist[0])
    del mylist[0]
    print('now my list is:',mylist)
#len()返回长度,sort()后按字典序排序，append会在末尾添加新的字符
    

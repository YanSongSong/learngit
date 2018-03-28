text='''\
Use python in order to write diary
It sounds really cool
Isn't it?
Everybody follow me:
Python NB
'''
f=open('diary.txt','w')
f.write(text)
f.close()
#upper case is how to use python to write
#down case is how to use python to read
f=open('diary.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line,end='')
f.close()

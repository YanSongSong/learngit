ab={
    'Swaroop':'swaroop@swaroop.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
    }

print("Swaroop's address is",ab['Swaroop'])


#删除一堆键值键配对
del ab['Larry']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name,address in ab.items():
    print('Contact {} at {}'.format(name,address))
#添加一对键值-值配对
ab['Guido']='guido@python.org'

if 'Guido'in ab:
    print("\nGuido's address is",ab['Guido'])

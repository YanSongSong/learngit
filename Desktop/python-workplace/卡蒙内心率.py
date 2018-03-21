#卡蒙内心率
RestingPulse=int(input('Resting Pulse:'))
age=(int(input('Age:')))
print('Intensity| Rate')
print('---------|------')
for i in range(55,100,5):
    print(str(i)+'%','   v|'+str(((((220-age)-RestingPulse)*i/100))+RestingPulse)+'bpm')


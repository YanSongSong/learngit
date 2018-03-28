import re
firstName=input('Enter the first name:')
lastName=input('Enter the last name:')
ZIPCode=input('Enter the ZIP Code:')
employeeId=input('Enter an employee ID:')
def checkName1(firstName,lastName):
    if(firstName==''):
        print('The first name must be filled in')
    elif(lastName==''):
        print('The last name must be filled in')
def checkName2(firstName,lastName):
    if(len(firstName)<2 and firstName!=''):
        print('"{}" is not a valid first name. It is too short.'.format(firstName))
    if(len(lastName)<2 and lastName!=''):
        print('"{}" is not a valid first name. It is too short.'.format(lastName))
def checkZIPCode(ZIPCode):
    if(not ZIPCode.isdigit()):
        print('The ZIP Code must be numeric.')
def checkemployeeId(employeeId):
    if(employeeId!='[A,Z][A,Z]-[0,9][0,9][0,9][0,9]'):
        print('{} is not a valid ID'.format(employeeId))
checkName1(firstName,lastName)
checkName2(firstName,lastName)
checkZIPCode(ZIPCode)
checkemployeeId(employeeId)


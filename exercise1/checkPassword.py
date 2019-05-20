import re
userInput = input('Enter your password: ')

def checkPassword():
    check = re.compile(r'[a-zA-Z0-9]{8,15}')
    resultConfirmed = check.search(userInput)
    print('Welcome ' + resultConfirmed.group())
checkPassword()
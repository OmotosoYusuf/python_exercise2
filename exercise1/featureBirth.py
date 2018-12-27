from datetime import date
print('Kindly type in your name')
myName = input()
print('Welcome,' + myName + '. This script allows you to check for your age.\n')

print('Press F/f to calculate your Future Age \nPress P/p to calculate Present Age \nPress O/o to calculate how Old you were in the past year \nType your choice and press Enter')

userInput = input()
if userInput == 'F' or userInput == 'f':
    print('What is your Year of Birth pls?')
    YOB = input()
    today = date.today()
    presentAge = today.year - int(YOB)
    print('What year will you like to check for')
    futureYear = input()
    futureAge = int(futureYear) - today.year
    realFuAge = int(presentAge) + int(futureAge)
    print('Your age in ' + str(futureYear) + ' will be ' + str(realFuAge))
elif userInput == 'P' or userInput == 'p':
    print('What is your Year of Birth pls?')
    YOB = input()
    today = date.today()
    presentAge = today.year - int(YOB)
    print('You present age as at ' + str(today.year) + ' is ' + str(presentAge))
elif userInput == 'O' or userInput == 'o':
    print('What is your Year of Birth pls?')
    YOB = input()
    print('What year will you like to check?')
    oldYear = input()
    presentAge = int(oldYear) - int(YOB)
    print('Your age as at ' + str(oldYear) + ' is ' + str(presentAge))
    
else:
    print('Please type a valid option')
    
    
##print('Can you enter your age please')
##usersAge = input()
##print('What year will you like to check for')
##usersYear = input()
##
##today = date.today()
##calcu = int(usersYear) - today.year
##
##addCalcu = int(usersAge) + int(calcu)
##print('Your age in ' + str(usersYear) + ' will be ' + str(addCalcu))

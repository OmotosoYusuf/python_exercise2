##def spam():
##	eggs = 99
##	bacon()
##	print(eggs)
##def bacon():
##     ham = 101
##     egg = 0
##spam()
##
##def spam():
##    print(eggs)
##eggs = 42
##spam()
##
##print('Your First Name')
##name = input()
##if name == 'Alice' or name == 'Bob':
##    print('Welcome ' + name)
##else:
##    print('try again')


##print('Enter a number')
##n = int(input())
##result = 0
##for number in range(n):
##    result = result + number
##print(result)

for number in range(1,10):
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    else:
        print(number)
    

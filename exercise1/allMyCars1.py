##print('Enter the name of car 1:')
##car1 = input()
##print('Enter the name of car 2:')
##car2 = input()
##print('Enter the name of car 3:')
##car3 = input()
##print('Enter the name of car 4:')
##car4 = input()
##print('Enter the name of car 5:')
##car5 = input()
##print('Enter the name of car 6:')
##car6 = input()
##print('The car names are:')
##print(car1 + ' ' + car2 + ' ' + car3 + ' ' + car4 + ' ' + car5 + ' ' + car6)

carNames = []
while True:
    print('Enter the name of car ' + str(len(carNames) + 1)
          + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    carNames = carNames + [name] #list concatenation
print('The car names are:')
for name in carNames:
    print(' ' + name)

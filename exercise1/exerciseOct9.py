spam = ['apples', 'bananas', 'tofu', 'cats']

def func(listValue):
    for i in range(len(listValue[:-2])):
        print(str(listValue[i]), end = ', ')
        continue
    print(str(listValue[-2]) + ' and ' + str(listValue[-1]))
##listValue = spam
func(spam)

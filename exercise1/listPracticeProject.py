##spam = ['apples', 'bananas', 'tofu', 'cats']
##
##def newList(spam):
##    spam.insert(-2, 'and')
##    spam = ', '.join(spam)
##    print(spam)
##
##def toString(arr):
##    s = ''
##    for i in range(len(arr)):
##        if i > 0:
##            if i == len(arr) - 1:
##                # last one
##                s = s + ' and '
##            else:
##                # second, third, ...
##                s = s + ', '
##        s = s + arr[i];
##    return s
##

##def comma(aList):
##    newList = []
##    for i in range(len(aList)-1):
##        newList.append(aList[i]+',')
##    newList.append('and '+aList[-1])
##    return newList
##spam = ['apples', 'bananas', 'tofu', 'cats']
##
##print (comma(spam))

spam = ['zero', 'one', 'two', 'three', 'second to last', 'last']

def func(listValue):
    print('\'', end='')    # Openning single quote.
    for i in range(len(listValue[:-2])):    # Iterate through all values in the list up to second to last.
        print(str(listValue[i]), end=', ')
        continue
    print(str(listValue[-2]) + ' and ' + str(listValue[-1]) + '\'')    # Add second to last and last to string separated by 'and'. End with a single quote.

##listValue = spam
func(spam)

    # Will do for any list.

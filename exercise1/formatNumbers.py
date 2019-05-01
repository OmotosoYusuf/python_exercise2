#! python3
# formatNumber.py - removes the starting 0 of a number
# put the number on different lines
# add the +234 nigeria code
# copy the number and print the result

import pyperclip
number = pyperclip.paste()

#remove, seperate and add prefix phone code
number = number.split(',')
#number = number.remove(number[0])
for i in range(len(number)): # loop through the number and add the phone code
    number[i] = '+234' + number[i]
print(pyperclip.copy(number))
    

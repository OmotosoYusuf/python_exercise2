#! python3
# this program checks for a nigeria phone number(s) in a chunk of text without using regular expression
# using regular will even make the code quicker to write, smaller and smarter

def isNumberNigeria(text):
    if len(text) != 11:
        return False
    for i in range(0, 11):
        if not text[i].isdecimal():
            return False
    return True

message = input('Enter or paste your document/text here: ')
for i in range(len(message)):
    chunk = message[i:i+11]
    if isNumberNigeria(chunk):
        print(chunk) 
print('Done')

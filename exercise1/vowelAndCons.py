##vowels = ['a', 'e', 'i', 'o', 'u']
##vowel = 0
##consonant = 0
##
##print('Enter your words')
##word = input()
##for i in word:
##    if i in vowels[0:6]:
##        vowel += 1
##        print('we have ' + str(vowel) + ' vowel' +'(s)')
##    
##    else:
##        consonant +=1
##        print('We have ' + str(consonant) + ' consonant' + '(s)')
##       
##    
##        
##        

print('Enter your words')
word = input()
vowels = 0
consonant = 0
for i in word:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ):
        vowels = vowels + 1
    else:
        consonant = consonant + 1
        print('Number of vowels ' + str(vowels))

import sys

user1 = input('Kindly enter your name ')
user2 = input('Enter your name too ')
user1Answer = input('%s, Will you like to pick a rock, paper or scissors' % user1)
user2Answer = input('%s, Will you like to pick a rock, paper or scissors' % user2)

def compare(u1,u2):
    if u1 == u2:
        return('It is a tie!')
    elif u1 == 'rock' and u2 == 'scissors':
        return('Rock wins!')
        else:
            return('Paper wins!')
    elif u1 == 'scissors' and u2 == 'paper':
        return('Scissors win!')
        else: 
            return('Rock wins!')
    elif u1 == 'paper' and u2 == 'rock':
        return('Paper wins!')
        else:
            return('Scissors win!')
    else:
        return('Invalid input! You have not entered rock, paper or scissors, try again.')
        sys.exit()

print(compare(user1Answer,user2Answer))

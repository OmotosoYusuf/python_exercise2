import sys

user1 = input('What is your name ')
user2 = input('And your name ')
user1Answer = input("%s, do you want to choose rock, paper or scissors? " % user1)
user2Answer = input("%s, do you want to choose rock, paper or scissors? " % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return('Rock wins!')
        else:
            return('Paper wins!')
    elif u1 == 'scissors':
        if u2 == 'paper':
            return('Scissors Win!')
        else:
            return('Rock Wins!')
    elif u1 == 'paper':
        if u2 == 'rock':
            return('Paper Wins!')
        else:
            return('Scissors Win!')
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()
    
print(compare(user1Answer, user2Answer))
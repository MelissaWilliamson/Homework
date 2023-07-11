import random
## Imported a random generator

options = ('rock', 'paper', 'scissors')
## added values for options

players_choice = input("Choose Rock, Paper, Or Scissors: ")
## added the input - prompts the input rock, paper or scissors

computer_choice = random.choice(options)
## assigned the random generator to the computers choice

print('You Chose:', players_choice)
print('Computer Chose:', computer_choice)

if  players_choice == computer_choice:
    print("It's a Tie")
elif players_choice == 'rock' and computer_choice == 'scissors':
    print('You Win')
elif players_choice == 'paper' and computer_choice == 'rock':
    print('You Win')
elif players_choice == 'scissors' and computer_choice == 'paper':
    print('You Win')
else:
    print('Computer Wins')
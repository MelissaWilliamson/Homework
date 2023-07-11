##Rock Paper Scissors Game

import random

def player_options(Rock, Paper, Scissors):
    print('Welcome to our game')
    options = ('Rock', 'Paper', 'Scissors:')
player_options('R=Rock', 'P=Paper', 'S=Scissors')

players_choice = input("Player choose Rock, Paper Or Scissors: ")

def computer_options(Rock, Paper, Scissors):
    print('Computer choose Rock, Paper Or Scissors')
    options = ('Rock', 'Paper', 'Scissors')
computer_options('0=Rock', '1=Paper', '2=Scissors')

players_choice = player_options('R', 'P', 'S')
computer_choice = computer_options('0', '1', '2')

print('You Chose:', players_choice)
print('Computer Chose:', computer_choice)

if players_choice == computer_choice:
    print("It's a Tie")
elif players_choice == 'Rock' and computer_choice == 'Scissors':
    print('You Win')
elif players_choice == 'Paper' and computer_choice == 'Rock':
    print('You Win')
elif players_choice == 'Scissors' and computer_choice == 'Paper':
    print('You Win')
else:
    print('Computer Wins')



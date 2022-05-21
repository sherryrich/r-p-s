# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# CONSTANTS
LIST = ['Rock', 'Paper', 'Scissors']

# Game
while True:
# Takes user input and assigns a value
    print('Please enter your input, please select either 1, 2 or 3')
    print('1 = Rock, 2 = Paper & 3 = Scissors')
    user_input = int(input())

    # Input validation
    if user_input is not [1,2,3]:
        print('You have not entered a valid option of number: 1 , 2 or 3')
    else:
        pass

    # Vars

    # handles computer decision
    comp_decision = random.choice([0,1,2])    
    computer_decision = LIST[comp_decision]
    user_input = LIST[user_input -1]
    print(f'{user_input } vs. {computer_decision}')
    # This handles compare between user input and computer rand choice
    # Code credit to Gerry
    if user_input == computer_decision:
        print("It's a draw!")
    elif (user_input == 'rock' and computer_decision == 'scissors') or (user_input == 'scissors' and computer_decision == 'paper') or (user_input == 'paper' and computer_decision == 'rock'):
        print('You win!')
    else:
        print('You lose')

    play_again = input("Wanna play again? y/n")
    if play_again.lower() != "y":
        break
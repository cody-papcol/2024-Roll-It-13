# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks if user inputted valid response
        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('please enter yes / no')

# defines the instructions
def instructions():
    print('''
    
    **** Instructions ****
    
    To being, decide on a score goal (eg: The first on to get a score of 50 wins).
    
    For each round of the game, you win points by rolling dice.
    The winner of the round is the one who gets 13 (or slightly less).
    
    If you win the round, then your score will increase by the number of points that you earned.
    If your first roll of two dice is a double (eg: both dice show a three),
    then your score will be DOUBLE the number of points.
    
    If you lose the round, then you don't get any points.
    
    If you and the computer tie (eg: you both get a score of 11), then you will have 11 points added to your score.
    
    Your goal is to try to get to the target score before the computer.
    
    Good luck.
    
    ''')

# Checks that users enter an integer that is more than 13
def int_check():
    while True:

        # Defining error var
        error = 'Please enter an integer that is 13 or more'

        # Getting input from user
        try:
            response = int(input('Enter an integer: '))

            # Checks if input integer is in acceptable range (integer is more than 13)
            if response < 13:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

# prints the name of the game
print()
print('🎲🎲 Roll It 13 🎲🎲')
print()

# checks if user wants to see instructions, if yes then prints instructions, if no then program continues
want_instructions = yes_no('Do you want to read the instructions? ')
if want_instructions == 'yes':
    instructions()

target_score = int_check()
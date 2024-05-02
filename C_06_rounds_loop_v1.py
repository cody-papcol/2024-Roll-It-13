# Checks that users enter an integer that is more than 13
def int_check(question):
    while True:

        # Defining error var
        error = 'Please enter an integer that is 13 or more'

        # Getting input from user
        try:
            response = int(input('Enter a target score: '))

            # Checks if input integer is in acceptable range (integer is more than 13)
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# main routine starts here

# initialise user score and computer score
user_score = 0
computer_score = 0

target_score = int_check('Enter a target score: ')
print(target_score)

while user_score < target_score and computer_score < target_score:
    print('Round heading goes here...')
    add_points = int(input('How many points have been won?'))
    user_score += add_points

print()
print(f'Your final score is {user_score}')

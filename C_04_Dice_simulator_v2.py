import random


# generates an integer between 0 and 6 to simulate rolling a die
def roll_die():
    result = random.randint(1, 6)
    return result


def two_rolls():
    double_score = 'no'

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = 'yes'

    # find the total points
    user_points = roll_1 + roll_2

    # show the user the result
    print(f'Die 1: {roll_1} \t Die 2: {roll_2}')

    return user_points, double_score


# Main routine starts here

how_many = int(input('How many dice? (please enter an integer) '))

for item in range(0, 10):

    if how_many == 2:
        start_points = two_rolls()
        points = start_points[0]
        double_points = start_points[1]

        print(f'You have {points} points and a double score of {double_points}')

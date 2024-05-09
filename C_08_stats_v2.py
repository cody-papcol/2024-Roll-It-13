# finds the lowest, highest and average score from a list
def get_stats(stats_list):

    # sort the lists
    stats_list.sort()

    # find lowest, highest, and average scores...
    lowest_score = user_scores[0]
    highest_score = user_scores[-1]
    average_score = sum(user_scores) / len(user_scores)

    return [lowest_score, highest_score, average_score]


# create lists to hold user and computer scores
user_scores = [11, 0, 13, 12, 11, 0]
computer_scores = [0, 0, 13, 12, 0, 12]

# loop six times - for testing purposes, ask the user to enter
# the score for the user and the computer for each round
# for item in range(0, 6):
#    user_points = int(input('Enter the user score: '))
#    computer_points = int(input('Enter the computer score: '))
#
#    # add user and computer score to lists!
#    user_scores.append(user_points)
#    computer_scores.append(computer_points)

# calculate the lowest, highest and average scores
# and display them.

user_stats = get_stats(user_scores)
computer_stats = get_stats(computer_scores)

print()
print('📊📊📊 Game Statistics 📊📊📊')
print()
print('     User')
print('Lowest Score: ', user_stats[0])
print('Highest Score: ', user_stats[1])
print('Average Score: ', user_stats[2])
print()
print('     Computer')
print('Lowest Score: ', computer_stats[0])
print('Highest Score: ', computer_stats[1])
print('Average Score: ', computer_stats[2])

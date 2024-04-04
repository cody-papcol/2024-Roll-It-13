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


target_score = int_check()
print(target_score)
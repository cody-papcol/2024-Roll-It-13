
while True:

    # Defining error var
    error = 'Please enter an integer that is 13 or more'

    # Getting input from user
    try:
        my_num = int(input('Enter an integer: '))

        # Checks if input integer is in acceptable range (integer is more than 13)
        if my_num < 13:
            print(error)

        else:
            print('Your number is', my_num)

    except ValueError:
        print(error)


print('🎲🎲 Roll It 13 🎲🎲')

# Test loop
while True:
    want_instructions = input('Do you want to read the instructions? ').lower()

# checks if user inputted valid response
    if want_instructions == 'yes' or want_instructions == 'y':
        print('you chose yes')
    elif want_instructions == 'no' or want_instructions == 'n':
        print('you chose no')
    else:
        print('you did not choose a valid response')



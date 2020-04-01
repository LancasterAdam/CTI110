# CTI-110
# P3HW1 - Color Mixer
# Adam Lancaster
# 3/31/20
#

repeat = 'y'                            # set initial repeat flag value.
validInput1 = 'n'                       # set initial validInput1 flag value.
validInput2 = 'n'                       # set initial validInput2 flag value.

while repeat == 'y':                    # loop to speed up repeated tests.
    
    while validInput1 == 'n':                   # check for validInput1 flag.
        c1 = str(input('enter first color: '))  # input for first color. 
        if c1 == 'red':                         # check 1st input for red.
            validInput1 = 'y'                   # validate 1st for red.
        elif c1 == 'blue':                      # check 1st input for blue.
            validInput1 = 'y'                   # validate 1st for blue.
        elif c1 == 'yellow':                    # check 1st input for yellow.
            validInput1 = 'y'                   # validate 1st for yellow.
        else:                                   # check for all other inputs.
            validInput1 = 'n'                   # reject all other inputs.
        if validInput1 == 'n':                  # if input invalid, notify user.
            print('invalid color. ')

    while validInput2 == 'n':                   # check for validInput2 flag.
        c2 = str(input('enter second color: ')) # input for second color.
        if c2 == 'red':                         # check 2nd input for red.
            validInput2 = 'y'                   # validate 2nd for red.
        elif c2 == 'blue':                      # check 2nd input for blue.
            validInput2 = 'y'                   # validate 2nd for blue.
        elif c2 == 'yellow':                    # check 2nd input for yellow.
            validInput2 = 'y'                   # validate 2nd for yellow.
        else:                                   # check for all other inputs.
            validInput2 = 'n'                   # reject all other inputs.
        if validInput2 == 'n':                  # if input invalid, notify user.
            print('invalid color. ')

    if c1 == 'red':                             # check c1 for red.
        if c2 == 'blue':                        # check c2 for blue.
            print('new color is purple.')       # output for purple.
        elif c2 == 'yellow':                    # check c2 for yellow.
            print('new color is orange.')       # output for orange. 
        else:                                   # check c2 for red.
            print('red, no change.')            # output for red.

    elif c1 == 'blue':                          # check c1 for blue.
        if c2 == 'red':                         # check c2 for red.
            print('new color is purple.')       # output for purple.
        elif c2 == 'yellow':                    # check c2 for yellow.
            print('new color is green.')        # output for green.
        else:                                   # check c2 for blue.
            print('blue, no change.')           # output for blue.

    else:                                       # check c1 for yellow.
        if c2 == 'red':                         # check c2 for red.
            print('new color is orange.')       # output for orange.
        elif c2 == 'blue':                      # check c2 for blue.
            print('new color is green.')        # output for green.
        else:                                   # check c2 for yellow.
            print('yellow, no change.')         # output for yellow.

    repeat = str(input('mix again? (y/n) '))    # ask user to repeat program.
        if repeat == 'y':                       # check for repeat flag.
            validInput1 = 'n'                   # reset flag for new mix.
            validInput2 = 'n'                   # reset flag for new mix.
        else:                                   # check for repeat flag.
            print('done.')                      # respond and finish. 


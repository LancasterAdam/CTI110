# CTI-110
# P3HW1 - Color Mixer
# Adam Lancaster
# 3/31/20
#

c1 = 'white'                                            # initial value.
c2 = 'black'                                            # initial value.

while c1 != ('red' or 'blue' or 'yellow'):              # get color 1 input
    c1 = str(input('enter first color to be mixed: '))  # while rejecting 
    if c1 != ('red' or 'blue' or 'yellow'):             # invalid colors.
        print('invalid color.')

while c2 != ('red' or 'blue' or 'yellow'):              # get color 2 input
    c2 = str(input('enter second color to be mixed: ')) # while rejecting
    if c2 != ('red' or 'blue' or 'yellow'):             # invalid colors.
        print('invalid color.')

if c1 == 'red':                                         # check c1 for red.
    if c2 == 'blue':                                    # check c2 for blue.
        print('new color is purple.')                   # output for purple.
    elif c2 == 'yellow':                                # check c2 for yellow.
        print('new color is orange.')                   # output for orange. 
    else:                                               # check c2 for red.
        print('red, no change.')                        # output for red.

elif c1 == 'blue':                                      # check c1 for blue.
    if c2 == 'red':                                     # check c2 for red.
        print('new color is purple.')                   # output for purple.
    elif c2 == 'yellow':                                # check c2 for yellow.
        print('new color is green.')                    # output for green.
    else:                                               # check c2 for blue.
        print('blue, no change.')                       # output for blue.

else:                                                   # check c1 for yellow.
    if c2 == 'red':                                     # check c2 for red.
        print('new color is orange.')                   # output for orange.
    elif c2 == 'blue':                                  # check c2 for blue.
        print('new color is green.')                    # output for green.
    else:                                               # check c2 for yellow.
        print('yellow, no change.')                     # output for yellow.

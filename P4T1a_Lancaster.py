# CTI-110
# P4T1a: Shapes
# Adam Lancaster
# 4/1/20
#

import turtle                               # import turtle package.

size = 10                                   # set size to 5. 

turtle.showturtle()                         # show the turtle.
turtle.left(180)                            # orient turtle properly to start.
turtle.speed(0)                             # set turtle speed.

for x in range (100):                       # make 100 shapes.
    for y in range (4):                     # make shape 4 sided.
        turtle.forward (size)               # size of shape.
        turtle.right (90)                   # angle of corner.
    else:                                   # at end of loop, increase size.
        size += 3                           # set increment to increase by.

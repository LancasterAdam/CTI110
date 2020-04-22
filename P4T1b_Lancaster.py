# CTI-110
# P4T1b: Initials
# Adam Lancaster
# 4/1/20
#

import turtle                           # import turtle package.
turtle.showturtle()                     # display the turtle.
turtle.speed(0)                         # set speed of turtle.
turtle.setup(800, 350)                  # set window to fit image.
turtle.pencolor('yellow')               # set line color.
turtle.pensize(5)                       # adjust line width.
turtle.bgcolor('green')                 # set background color.

turtle.penup()                          # move from point to point to make the 
turtle.goto(-350, -100)                 # letter "A".
turtle.pendown()
turtle.goto(-250, 100)
turtle.goto(-200, 0)
turtle.goto(-300, 0)
turtle.goto(-200, 0)
turtle.goto(-150, -100)
turtle.penup()

turtle.goto(-100, 100)                  # move from point to point to make the
turtle.pendown()                        # letter "T".
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, -100)
turtle.penup()

turtle.goto(150, 100)                   # move from point to point to make the
turtle.pendown()                        # letter "L".
turtle.goto(150, -100)
turtle.goto(350, -100)

turtle.hideturtle()                     # stop displaying turtle. 


# configure turtle window and speed
# move turtle point to pinbt to create initials

# CTI-110
# P3HW2 - BasicMath
# Adam Lancaster
# 4/1/20
#

repeat1 = 'y'                                           # set repeat flag 1.
repeat2 = 'y'                                           # set repeat flag 2.

while repeat1 == 'y':                                   # check for repeat flag.
    
    number1 = int(input('Enter first number: '))        # input for number 1.
    number2 = int(input('Enter second number: '))       # input for number 2.

    while repeat2 == 'y':                               # check for repeat flag.
        
        print('--------MENU--------')                   # display menu.
        print('1) Add Numbers')
        print('2) Multiply Numbers')
        print('3) Subtract Numbers')
        print('4) Exit')
        print('--------------------')
                                                        # input for formula.
        math = str(input('Choose function: (1/2/3/4): '))

        if ((math == '1') or (math == '2') or +         # validate entry.
            (math == '3') or (math == '4')):
            repeat2 = 'n'

        else:                                           # reject entry. 
            print('Invalid entry. ')

    if math == '1':                                     # addition check.
        output = number1 + number2                      # addition output.
        print(output)

    elif math == '2':                                   # multiply check.
        output = number1 * number2                      # multiply output.
        print(output)

    elif math == '3':                                   # subtract check.
        output = number1 - number2                      # subtract output.
        print(output)

    else:                                               # exit check.
        print('Program will terminate.')                # exit output.

    repeat2 = 'y'                                       # reset flag.
    
    repeat1 = str(input('Calculate again? (y/n) '))     # input for repeat flag.
    if repeat1 == 'n':                                  # check for repeat flag.
            print('Program will terminate.')            # exit output.


# get number inputs
# choose operation
# display output 
# queue for repeat

# Math Quiz Generator
# 4/30/20
# CTI-110 P5HW2 PART2B - Math Quiz
# Adam Lancaster
#

def menu():
# display menu with options for add, subtract, and exit. Queue user to make
# selection, then validate that input is 1, 2, or 3.
    print()
    print('{:^30}'.format('MAIN MENU'))
    print('-' * 30)
    print('{:^30}'.format('1) ADD RANDOM NUMBERS'))
    print()
    print('{:^30}'.format('2) SUBTRACT RANDOM NUMBERS'))
    print()
    print('{:^30}'.format('3) EXIT'))
    print('-' * 30)
    print()
    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input('MAKE SELECTION: (1/2/3) '))
    return choice
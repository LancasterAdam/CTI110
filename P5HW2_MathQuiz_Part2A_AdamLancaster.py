# Math Quiz Generator
# 4/30/20
# CTI-110 P5HW2 PART2A - Math Quiz
# Adam Lancaster
#

import random
import P5HW2_MathQuiz_Part2B_AdamLancaster as part2B

def main():
# display menu and queue user to make selection. depending on input, generate
# a random addition or subtraction problem and queue user to input solution.
# if solution is correct, congratulate user. if incorrect, alert user and 
# display the correct answer. program will only terminate when user selects
# exit (enters '3') from the main menu.
    repeat = 1
    while repeat == 1:
        choice = part2B.menu()
        if choice == 1:
            addNumbers()
        elif choice == 2:
            subtractNumbers()
        else:
            # due to input validation the only value that can reach this
            # point is '3', despite it not being explicitly stated in this
            # part of the code.
            break
    print('PROGRAM WILL TERMINATE.')
    
def addNumbers():
# generates 2 random numbers, displays an addition problem and queues user
# for input. if answer is correct, congratulate user. if incorrect, alert user
# and display correct answer.
    number1, number2 = numberGenerator()
    correctSolution = number1 + number2
    userSolution = displayAddProblem(number1, number2)
    result(userSolution, correctSolution)

def subtractNumbers():
# generates 2 random numbers, displays an addition problem and queues user
# for input. if answer is correct, congratulate user. if incorrect, alert user
# and display correct answer.
    number1, number2 = numberGenerator()
    correctSolution = number1 - number2
    userSolution = displaySubProblem(number1, number2)
    result(userSolution, correctSolution)

def numberGenerator():
# generate 2 random numbers between 1 and 1000, then return those numbers.
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    return number1, number2

def displayAddProblem(number1, number2):
# display math problem and queue user to enter solution. returns value.
    print()
    print('{:>5}'.format(number1))
    print("+", end='')
    print('{:>4}'.format(number2))
    userSolution = int(input('= '))
    return userSolution

def displaySubProblem(number1, number2):
# display math problem and queue user to enter solution. returns value.
    print()
    print('{:>5}'.format(number1))
    print("-", end='')
    print('{:>4}'.format(number2))
    userSolution = int(input('= '))
    return userSolution

def result(userSolution, correctSolution):
# check if user solution is correct by comparing to correct solution. if
# values are equal, congratulate user. if they dont match, tell user they
# are incorrect and then show correct solution.
    if userSolution == correctSolution:
        print('CONGRATULATIONS, YOU ARE CORRECT!')
    else:
        print('INCORRECT. THE CORRECT ANSWER WAS', correctSolution)

main()
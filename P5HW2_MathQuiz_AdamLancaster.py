# Math Quiz Generator
# 4/30/20
# CTI-110 P5HW2 - Math Quiz
# Adam Lancaster
#

import random

def main():
# generate 2 random numbers to be added and queue user to enter total. if
# correct, congratulate user. if incorrect, show user correct answer.
    number1, number2, correctSolution = numberGenerator()
    userSolution = displayProblem(number1, number2)
    result(userSolution, correctSolution)
    
def numberGenerator():
# generate 2 random numbers between 1 and 1000, then return those numbers.
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    correctSolution = number1 + number2
    return number1, number2, correctSolution

def displayProblem(number1, number2):
# display math problem and queue user to enter solution. returns entered value.
    print('QUIZ')
    print()
    print('{:>5}'.format(number1))
    print("+", end='')
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
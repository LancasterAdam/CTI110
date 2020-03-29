# The Rude Calculator: It can only multiply and add. And its not cool about it.
# 3/28/20
# CTI-110 P2HW1 - Basic Math
# Adam Lancaster
#

firstNumber = int(input('Gimme the first number! '))
print("That's a stupid number and you're stupid for entering it. ")
secondNumber = int(input("What're you waiting for, gimme the second one! "))

newSum = str(firstNumber + secondNumber) + ","
newProduct = str(firstNumber * secondNumber) + "."
secondNumber = str(secondNumber) + "."

print('Ok dummy, the numbers you entered were', firstNumber,
      'and', secondNumber)
print('The sum of those AWFUL numbers is', newSum,
      'and the product is', newProduct)
print('Now leave me alone!')


# program works as follows:
#
# get input for first number
# insult first number and user
# get input for second user
#
# perform addition, then convert to str and add punctuation
# perform multiplication, then convert to str and add punctuation
# turn second number into str and add punctuation
#
# insult numbers and user, then state entered numbers
#
# insult numbers and state sum and product
#
# be rude

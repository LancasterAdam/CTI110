# CTI-110
# P4HW1 - Expenses
# Adam Lancaster
# 4/3/20

exp = []                                                # create expense list.

account = float(input('enter account balance: '))       # get account balance.

repeat = 'y'                                            # set repeat flag.

while repeat != 'n':                                    # set input loop.

    exp.append(int(input('enter expense amount: ')))    # add expense to list.
    repeat = str(input('add another expense? (y/n)'))   # ask for repeat.

expNum = len(exp)                                       # get list length.

expTotal = 0                                            # set exp starting value

while len(exp) > 0:                                     # if list has contents,
        expTotal += exp[0]                              # read 1st value, add to
        exp.pop(0)                                      # total, clear entry.

balance = format(account - expTotal, ',.2f')            # calculate balance.

print('starting acount balance: $',
    format(account, ',.2f'))                            # show starting balance.

print('number of expenses entered:', expNum)            # show # of expenses.
        
print('balance after expenses: $', balance)             # show final balance.
    

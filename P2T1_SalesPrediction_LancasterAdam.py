# Predict profits from total sales projections
# 3/28/20
# CTI-110 P2T1 - Sales Prediction
# Adam Lancaster
#

# get projected total sales input
totalSales = float(input('Enter projected total sales: $ '))

# calculate profits as 23 perfcent of total sales and format for currency.
profit = totalSales * .23

# display the profit
print('projected profits: $', format(profit, '.2f'))

# Bug Collector
# 4/2/20
# CTI-110 P4T2
# Adam Lancaster

total = 0                                               # set starting value.

for day in range (5):                                   # ask for input 5 times.
    total += int(input('enter day total: '))            # add inputs together.
    
print('total bugs collected for the week:', total)      # display output.

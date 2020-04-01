# Area of Rectangles Comparator
# 3/31/20
# CTI-110 P3T1 Area of Rectangles
# Adam Lancaster

repeat = 'y'                                                # WHILE loop
                                                            # to make testing
while repeat == 'y':                                        # faster

    r1Width = float(input('enter rectangle 1 width: '))     # input r1 width
    r1Height = float(input('enter rectangle 1 height: '))   # input r1 height

    r2Width = float(input('enter rectangle 2 width: '))     # input r2 width
    r2Height = float(input('enter rectangle 2 height: '))   # input r2 height

    r1Area = r1Width * r1Height                             # calculate r1 area 
    r2Area = r2Width * r2Height                             # calculate r2 area

    if r1Area > r2Area:                                     # output for r1 > r2
        print("rectangle 1's area is greater.")

    elif r1Area < r2Area:                                   # output for r1 < r2
        print("rectangle 2's area is greater.")

    else:                                                   # output for r1 = r2
        print("rectangles 1 and 2 have equal areas.")

    repeat = str(input('repeat? (y/n) '))                   # input for repeat

if repeat == 'n':                                           # output for done
    print('done.')

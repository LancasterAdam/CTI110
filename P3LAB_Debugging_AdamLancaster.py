# CTI-110
# P3LAB - Debugging
# Adam Lancaster
# 4/1/20
#

A_score = 90                                    # set value for A.
B_score = 80                                    # set value for B.
C_score = 70                                    # set value for C.
D_score = 60                                    # set value for D.

score = int(input('enter score: '))             # get input for score.

if score >= A_score:                            # check score for A value.
    print('Your grade is A. ')                  # output for A value.
else:
    if score >= B_score:                        # check score for B value.
        print('Your grade is B. ')              # output for B value.
    else:
        if score >= C_score:                    # check score for C value.
            print('Your grade is C. ')          # output for C value.
        else:
            if score >= D_score:                # check score for D value.
                print('Your grade is D. ')      # output for D value.
            else:                               # everything else is F.
                print('Your grade is F. ')      # output for F.

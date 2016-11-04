# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def diamond(number, db):
    if number%2 != 0:
            m = 1
            for i in range(number+1):
                if i < (number-1)//2:
                    print((int((number-m)/2)*" " + m*"*" + int((number-m)/2)*" ")*db)
                    m = m + 2
                elif i == (number-1)//2:
                    print((int((number-m)/2)*" " + m*"*" + int((number-m)/2)*" ")*db)
                else:
                    m = m - 2
                    print((int((number-m)/2)*" " + m*"*" + int((number-m)/2)*" ")*db)


    else:
        number = number + 1
        n = 1
        for i in range(number+1):
            if i < (number-1)//2:
                print((int((number-n)/2)*" " + n*"*" + int((number-n)/2)*" ")*db)
                n = n + 2
            elif i == (number-1)//2:
                print((int((number-n)/2)*" " + n*"*" + int((number-n)/2)*" ")*db)
            else:
                n = n - 2
                print((int((number-n)/2)*" " + n*"*" + int((number-n)/2)*" ")*db)



diamond(7, 7)

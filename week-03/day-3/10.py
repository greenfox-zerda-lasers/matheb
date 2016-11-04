# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle

def triangle(number):
    if number%2 != 0:
        n = 1
        for i in range(int((number-1)/2)+1):
            print(int((number-n)/2)*" " + n*"*" + int((number-n)/2)*" ")
            n = n + 2

    else:
        number = number + 1
        n = 1
        for i in range(int((number-1)/2)+1):
            print(int((number-n)/2)*" " + n*"*" + int((number-n)/2)*" ")
            n = n + 2

triangle(15)

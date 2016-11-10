# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count(number):
    if number <= 1: #base case
        print(1)
        return 1
    else:
        print(number)
        return number + count(number-1)

count(5)

# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def count(number):
    if number <= 1: #base case
        return 1
    else:
        return number + count(number-1)

print(count(5))

# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

def length(number):
    if number < 1: #base case
        return 0
    else:
        return int(number)%10 + length((number-1)/10)

print(length(1))
print(length(12))
print(length(123))
print(length(1234))

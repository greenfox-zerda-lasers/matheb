# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add(numbers):
    if len(numbers) == 0:
        return 0
    elif type(numbers[0]) == list:
        return add(numbers[0]) + add(numbers[1:])
    else:
        return numbers[0] + add(numbers[1:])

numbers = [1, 2, [3, 4], 1, [1, [2, 4]]]
print(add(numbers))

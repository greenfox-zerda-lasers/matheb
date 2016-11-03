numbers = [4, 5, 6, 7, 8, 9, 10]


def sum(numbers):
    i=0
    for j in range(len(numbers)):
        i = i + numbers[j]
        #print(numbers[j])
    print(i)

sum(numbers)
sum([2, 3, 4])

numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def rev(numbers):
    newlist = []
    for i in range(len(numbers)-1, -1, -1):
        print(numbers[i])
        newlist.append(numbers[i])


    print(newlist)


rev(numbers)

numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def filter_odd(list):
    newlist = []
    for i in range(len(list)):
        if list[i]%2 == 0:
            newlist.append(list[i])
        else:
            continue
    print(newlist)

filter_odd(numbers)
filter_odd([2, 2, 4, 3, 4, 5, 6, 7, 8, 9])

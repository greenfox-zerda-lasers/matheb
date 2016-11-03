#linear_search([4,5,6], 6)
# expected output: 2

#linear_search([4,5,7], 6)
# expected output: -1


def linear_search(list, item):
    value = -1
    for i in range(len(list)):
        if list[i] == item:
            value = list[i]
    print(value)


linear_search([1, 5, 2, 4, 1, 3, 0], 7)

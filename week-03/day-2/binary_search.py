def binary_search(list, item):
    isin = False
    list = sorted(list)
    n = int(len(list)/2)
    while n >= 0:
        if item == list[n]:
            isin = True
        elif item > list[n]:
            n = n + int(n/2)
        else:
            n = n - int(n/2)


    print(isin)

binary_search([2,3,2,4,8], 2)
binary_search([2,3,2,4,8], 6)
binary_search([2,3,2,4,8], 4)

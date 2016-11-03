#union([4,5,6], [1,2,3])
# expected output: [4,5,6,1,2,3]

#union([4,5,7], [4,1,7])
# expected output: [1,4,5,7]

def uni(first, second):
    united = first
    for i in range(len(second)):
        if second[i] not in united:
            united.append(second[i])

    print(united)

uni([1, 2, 3, 4], [1, 2, 5])

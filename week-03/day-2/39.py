names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def shortest(list):
    short = list[0]
    for i in range(1, len(list)):
        if len(list[i]) < len(short):
            short = list[i]
    print(short)

shortest(names)

# create a function that returns it's input factorial

def fact(number):
    j = 1
    for i in range(1, number+1):
        j = j * i

    print(j)

fact(3)
fact(5)

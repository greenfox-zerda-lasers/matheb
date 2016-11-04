def diamond(number):
    for i in range(number+1):
        x = (number//2)
        if i <= number//2+1:
            print(i*"*")
        else:
            print(x*"*")
            x = x-2

diamond(7)

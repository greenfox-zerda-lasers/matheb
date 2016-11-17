# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divideTen():
    number = int(input("Please add a number!"))
    return 10/number

while True:
    try:
        print(divideTen())
        break
    except ValueError:
        print("Are you sure, you gave a number?")
    except ZeroDivisionError:
        print("fail")

divideTen()

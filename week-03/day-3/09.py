# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def stars(number):
    for i in range(number+1):
        print(i * "*")


stars(10)

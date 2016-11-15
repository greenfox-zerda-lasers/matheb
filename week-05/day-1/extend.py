# Adds a and b, returns as result
def add(a, b):
    if type(a) != (int or float) or type(b) != (int or float):
        raise ValueError("please add strings")
    else:
        return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if type(a) != (int or float) or type(b) != (int or float) or type(c) != (int or float):
        raise ValueError("please add strings")
    else:
        if a > b:
            if b > c:
                return a
        elif b > c:
            return b
        else:
            return c


# Returns the median value of a list given as param
def median(pool):
    if type(pool) != list:
        pool = list(pool)
    pool.sort()
    for i in pool:
        if type(i) != int:
            raise ValueError("please add integers in the input list")
    if len(pool) % 2 != 0:
        median = pool[len(pool)//2]
        return median
    else:
        median = (pool[(len(pool)-1)//2] + pool[(len(pool)-1)//2+1]) / 2
        return median

# Returns true if the param is a vovel
def is_vovel(char):
    if type(char) != str:
        raise TypeError("please add strings")
    if len(char) > 1:
        raise ValueError("please add only one letter")
    char.lower()
    if char in 'aeiouéáőűöüóí':
        return True
    else:
        return False

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    if type(hungarian) != str:
        raise TypeError("please add strings")
    for i in hungarian:
        if i.isalpha() != True:
            raise TypeError("please add only letters")
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve

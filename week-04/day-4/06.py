# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).

def bunny_ears(bunnies):
    if bunnies % 2 == 0:
        if bunnies <= 2: #base case
            return 5
        else:
            return 5 + bunny_ears(bunnies-2)

    elif bunnies % 2 != 0:
        if bunnies <= 2: #base case
            return 2
        else:
            return 5 + bunny_ears(bunnies-2)

print(bunny_ears(30))
print(bunny_ears(5))

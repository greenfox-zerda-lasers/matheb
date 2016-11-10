# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def bunny_ears(bunnies):
    if bunnies <= 1: #base case
        return 1
    else:
        return 1 + bunny_ears(bunnies-1)

print(bunny_ears(25))

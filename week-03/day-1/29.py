ab = 123
credits = 100
is_bonus = False

if (credits >= 50) and (is_bonus == False) :
    ab = ab - 2
elif (credits < 50) and (is_bonus == False) :
    ab = ab - 1

print(ab)

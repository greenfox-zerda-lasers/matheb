# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separate(something):
    if len(something) <= 1:
        return something[0]
    else:
        return something[0] + '*' + separate(something[1:])

print(separate('nxuszixul'))

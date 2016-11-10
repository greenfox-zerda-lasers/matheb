# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def delete_x(something):
    if len(something) == 0:
        return ''
    if something[0] == 'x' or something[0] == 'X':
        return '' + delete_x(something[1:])
    return something[0] + delete_x(something[1:])

print(delete_x('nxuszixul'))

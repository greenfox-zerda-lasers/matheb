# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def change_char(something):
    if len(something) == 0:
        return ''
    if something[0] == 'x':
        return 'y' + change_char(something[1:])
    return something[0] + change_char(something[1:])

print(change_char('nxuszixul'))

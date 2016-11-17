# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def countLines():
    text = input("Which file's lines would you like to count?")
    count = len(open(text).readlines(  ))
    return count

while True:
    try:
        print(countLines())
        break
    except IOError:
        print("zero")

countLines()

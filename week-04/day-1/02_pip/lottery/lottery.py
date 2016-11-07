# Create a method that returns the five most frequent lottery number in a pretty table format

def five_most_frequent():
    from collections import Counter
    from prettytable import PrettyTable

    fobj = open("otos.csv", "r")
    text = fobj.readlines()
    fobj.close()
    numbers = []

    #print(text)

    for line in text:
        listline = line.rstrip().split(";")
        numbers.extend(listline[11:16])


    #print(listline)
    #print(numbers)

    c = Counter(numbers)
    #print (c.most_common(5))
    top = c.most_common(5)

    table = PrettyTable(["number", "frequency"])
    for j in top:
        table.add_row(j)
    print(table)



print(five_most_frequent())

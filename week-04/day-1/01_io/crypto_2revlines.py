# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    fobj = open(file_name, 'r')
    lines = fobj.readlines()
    fobj.close()
    output = []
    #print(string)
    for line in lines:
        temp = line.rstrip()
        element =""
        for i in line[-2::-1]:
            element += i
        element += "\n"
        output.append(element)

    return''.join(output)

print(decrypt("texts/reversed_zen_lines.txt"))

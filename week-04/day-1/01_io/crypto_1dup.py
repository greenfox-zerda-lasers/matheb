# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    fobj = open(file_name, 'r')
    lines = fobj.readlines()
    fobj.close()
    output = []
    #print(string)
    for line in lines:
        temp = line.rstrip()
        element = ""
        for i in range(len(temp)):
            if i % 2 == 0:
                element += temp[i]

        element += "\n"
        output.append(element)

    return ''.join(output)


print(decrypt("texts/duplicated_chars.txt"))

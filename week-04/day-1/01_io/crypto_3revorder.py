# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    fobj = open(file_name, 'r')
    lines = fobj.readlines()
    fobj.close()
    output = []
    #print(string)
    for line in range(len(lines)-1, -1, -1):
        output.append(lines[line])

    return ''.join(output)

print(decrypt("texts/reversed_zen_order.txt"))

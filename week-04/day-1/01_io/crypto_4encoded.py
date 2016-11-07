# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    fobj = open(file_name, 'r')
    lines = fobj.readlines()
    fobj.close()
    output = []
    for line in lines:
        element = ""
        for char in line:
            if char == " ":
                newchar = ord(char)
            elif char == "\n":
                newchar = ord(char)
            else:
                newchar = ord(char)-1

            element += chr(newchar)
        output.append(element)

    return''.join(output)

print(decrypt("texts/encoded_zen_lines.txt"))

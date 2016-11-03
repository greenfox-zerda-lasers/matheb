def make_palindrom(something):
    palindrome = something
    for i in range(len(something)-1, -1, -1):
        palindrome = palindrome + something[i]
    print(palindrome)

make_palindrom("flower")

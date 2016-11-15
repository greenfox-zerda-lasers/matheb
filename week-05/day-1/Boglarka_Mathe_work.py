from string import punctuation

#Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
def anagramm(string1, string2):
    if type(string1) != str or type(string2) != str:
        raise ValueError("please add strings")
    string1 = string1.lower()
    string2 = string2.lower()
    for i in string1:
        if i == " ":
            string1 = string1.pop(i)
    for j in string2:
        if j == " ":
            string2 = string2.pop(j)
    if len(string1) != len(string2):
        return False
    else:
        list_string2 = list(string1)
        list_string1 = list(string2)
        list_string2.sort()
        list_string1.sort()
        if list_string2 == list_string1:
            return True
        else:
            return False

#Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
def count_letters(string):
    if type(string) != str:
        raise ValueError("please add string")
    string = list(string.lower())
    letterdict={}
    for letter in string:
        if letter.isalpha() == True:
            letterdict[letter] = 0
    for letter in string:
        if letter.isalpha() == True:
            letterdict[letter] += 1
    return letterdict

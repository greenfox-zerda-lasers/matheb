def collect_palindrom(text):
    palindrome = []
    candidates = []

    length = len(text)-1

    for i in range(0, length):
        for j in range(i+1, length+1):
            if text[i] == text[j]:
                if len(text[i:j+1]) >= 3:
                    candidates.append(text[i:j+1])

    for candidate in range(0, len(candidates)):
        if candidates[candidate] == candidates[candidate][::-1]:
            palindrome.append(candidates[candidate])
            #print(candidates[candidate])


    print(candidates)
    print(palindrome)

collect_palindrom("bennexkcdetet. rr b")

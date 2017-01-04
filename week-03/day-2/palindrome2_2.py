def collect_palindrom(list):
    palindrome = []
    n = 0
    m = 0
    for i in range(1, len(list)-1, 1):
        if list[i-n] == list[i+1+n]:
            while (list[i-n] == list[i+1+n]) and ((i-1)>=0):
                n += 1
            if len(list[i-n+1:i+n]) >= 3:
                palindrome.append(list[i-n+1:i+n])



    print(palindrome)

collect_palindrom("flowwwoer  error")

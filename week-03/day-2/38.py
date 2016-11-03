numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def list_min(list):
    find_min = []
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                find_min.append(list[i])

    #print(len(find_min))
    #print(find_min)
    print(find_min[len(find_min)-1])

list_min(numbers)

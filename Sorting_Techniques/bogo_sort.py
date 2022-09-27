from random import shuffle

def is_sorted(lst):
    for index in range(len(lst)-1):
        if lst[index] > lst[index+1]:
            return False
    return True


def bogo_sort(lst):
    while not is_sorted(lst):
        shuffle(lst)
    return lst


unsortedLst = [2, 1, 4, 3, 7, 6, 5, 8, 10, 9]
print(unsortedLst)
sortedLst = bogo_sort(unsortedLst)
print(sortedLst)

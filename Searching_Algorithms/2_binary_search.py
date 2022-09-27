def binary_search(lst, target):
    first = 0
    last = len(lst)-1

    while first<=last:
        mid = (first+last)//2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            first = mid+1
        elif lst[mid] > target:
            last = mid-1
    return None


x = (1, 2, 3, 4, 5, 6)
i = 4
position = binary_search(x, i)
print(f"index of {i} is {position}")

def merge_sort(lst):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    combine: Merge the sorted sublist created in previous step.
    
    Takes O(n log n) time 
    Space Complexity is linear
    """
    
    if len(lst) <= 1:
        return lst
    
    # Divide step
    left_half, right_half = split(lst)
    
    # Conquer step
    left = merge_sort(left_half)
    right = merge_sort(right_half) 
    
    # merging step
    return merge(left, right)

def split(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    
    Takes overall O(log n) time
    """
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    
    return left, right

def merge(left, right):
    """
    Merges two lists/arrays, sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0 # for indexes of left list
    j = 0 # for indexes of right list
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l


if __name__ == "__main__":
    unsortedList = [4, 2, 6, 1, 7, 8, 10, 9, 3, 5]
    sortedList = merge_sort(unsortedList)
    print(f"unsortedList--> {unsortedList}")
    print(f"sortedList-->, {sortedList}")
    
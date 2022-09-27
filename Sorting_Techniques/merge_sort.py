def merge_sort(lst):
    list_length = len(lst)
    if list_length <= 1:
        return lst
    # Divide step
    mid = list_length // 2
    left_list, right_list = lst[:mid], lst[mid:]
    # Conquer step
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    # merging step
    new_list = [] # Creating a new empty list
    left_index = 0
    right_index = 0
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            new_list.append(left_list[left_index])
            left_index += 1
        else:
            new_list.append(right_list[right_index])
            right_index += 1
    while left_index < len(left_list):
        new_list.append(left_list[left_index])
        left_index += 1
    while right_index < len(right_list):
        new_list.append(right_list[right_index])
        right_index += 1
    return new_list


if __name__ == "__main__":
    unsortedList = [4, 2, 6, 1, 7, 8, 10, 9, 3, 5]
    sortedList = merge_sort(unsortedList)
    print(f"unsortedList--> {unsortedList}")
    print(f"  sortedList--> {sortedList}")
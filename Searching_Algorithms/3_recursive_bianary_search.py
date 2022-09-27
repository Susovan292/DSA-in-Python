def recursive_binary_search(lst, target):
    if len(lst) == 0:
        return None
    else:
        midpoint = (len(lst)) // 2
        
        if lst[midpoint] == target:
            return midpoint
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint + 1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)


if __name__ == "__main__":
    x = (1, 2, 3, 4, 5, 6)
    x = []
    t = 4

    position = recursive_binary_search(x, t)
    print(f"index of {t} is {position}")

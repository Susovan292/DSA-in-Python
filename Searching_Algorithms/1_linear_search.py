def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i 
    return "Not Found"


if __name__ == "__main__":
    x = ('susovan', 'pratik', 'aniket', 'kunal', 'abhay', 'shubham')
    name = 'shubham'
    index = linear_search(x, name)
    print(f"found {name} at index {index}")

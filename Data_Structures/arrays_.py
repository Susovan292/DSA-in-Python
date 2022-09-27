import numpy as np

# Creating an array using numpy library
new_array = np.array([1, 2, 3]) 

# Creating an array/list using list() or []
new_list = [1, 2, 3, 4, 5]



# Doing some operations
print(new_list[3])

if 1 in new_array: print(True)

numbers = [] # creating a list

numbers.append(1) # takes constant space
numbers.append(2)
numbers.append(3)

numbers.extend([4, 5, 6, 7]) 

deleted_num = numbers.pop() # returns the last inserted item

print(len(numbers))
print(numbers)
print(deleted_num)
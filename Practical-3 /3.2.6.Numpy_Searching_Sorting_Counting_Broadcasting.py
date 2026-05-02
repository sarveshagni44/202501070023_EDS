#The given code in the editor takes a single array, array1, as space-separated integers as input from the user.
#Additionally, it takes the following inputs:
#search_value: The value to search for in the array.
#count_value: The value to count its occurrences in the array.
#broadcast_value: The value to add for broadcasting across the array.

# code : 

import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

indices = np.where(array1==search_value)[0]
print(indices)

counting = np.count_nonzero(array1==count_value)
print(counting)

brdcst = array1 + broadcast_value
print(brdcst)

sorting = np.sort(array1)
print(sorting)

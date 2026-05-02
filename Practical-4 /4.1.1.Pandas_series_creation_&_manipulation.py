#Write a Python program that takes a list of numbers from the user, creates a Pandas series from it,
#and then calculates the mean of even and odd numbers separately using the groupby and mean() operations.

#code : 

import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))

series=pd.Series(numbers)

grouped = series.groupby(series%2 == 0).mean()

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]
print("Mean of even and odd numbers:")
print(grouped)

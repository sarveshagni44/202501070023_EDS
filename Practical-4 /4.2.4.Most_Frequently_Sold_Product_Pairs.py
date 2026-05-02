#Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:
#The CSV file contains the following columns: Date, Product, Quantity, Price, and City.
#For each date, find all pairs of products that were sold together (i.e., two products sold on the same date).
#Output the product pair/s that was sold most frequently.

# code :

import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# Group products by date
grouped = df.groupby("Date")["Product"].apply(list)

# Count all product pairs
pair_counter = Counter()

# Generate all the unique pairs for the day
for Products in grouped:
	pairs = combinations(sorted(Products),2)
	pair_counter.update(pairs)

# Find the maximum frequency
if pair_counter:
	max_count = max(pair_counter.values())

# Get all pairs with maximum frequency
	most_frequent_pairs = [pair for pair, count in pair_counter.items() if count == max_count]

# Output results
	for pair in most_frequent_pairs:
		print(f"{pair[0]} and {pair[1]}: {max_count} times")
else:
	print("No product pairs found.")

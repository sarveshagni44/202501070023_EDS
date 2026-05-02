#Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:
#The CSV file contains the columns: Date, Product, Quantity, Price, and City.
#Group the data by Month and calculate the total sales for each month.
#Find the month with the highest total sales and display it.
#Also, display the total sales for the best month.

# code :

import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
df["Total sales"] = df["Quantity"] * df["Price"]

#Find the month with highest total sales
monthly_sales=df.groupby("Month")["Total sales"].sum()
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")

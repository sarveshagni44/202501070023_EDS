#You are provided with the Titanic dataset containing information about passengers on the Titanic. 
#Your task is to write Python code to answer the following questions based on the dataset.
#For each question, perform necessary data cleaning, transformations, and calculations as required.

# code :

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# 1. Display the first 5 rows of the dataset
print(data.head())

# 2. Display the last 5 rows of the dataset
print(data.tail())

# 3. Get the shape of the dataset
print(data.shape)

# 4. Get a summary of the dataset (info)
data.info()
print("None")
# 5. Get basic statistics of the dataset
print(data.describe())

# 6. Check for missing values
print(data.isnull().sum())

# 7. Fill missing values in the ‘Age’ column with the median age
data['Age'].fillna(data['Age'].median(),inplace=True)

# 8. Fill missing values in the ‘Embarked’ column with the mode
data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)

# 9. Drop the ‘Cabin’ column due to many missing values
data.drop('Cabin',axis=1,inplace=True)

# 10. Create a new column 'FamilySize’ by adding ‘SibSp' and ‘Parch'
data['Familysize'] = data['SibSp']+data['Parch']

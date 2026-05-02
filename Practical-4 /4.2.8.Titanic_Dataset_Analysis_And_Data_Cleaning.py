#You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.

# code :

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


# 1
print(data[data['Survived'] == 1]['Sex'].value_counts())

# 2
print(data[data['Survived'] == 0]['Sex'].value_counts())

# 3
print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

# 4
print(data[data['Survived'] == 0]['Embarked_S'].value_counts())

# 5
children = data[data['Age'] < 18]
print(children['Survived'].mean())

# 6
adults = data[data['Age'] >= 18]
print(adults['Survived'].mean())

# 7
print(data[data['Survived'] == 1]['Age'].median())

# 8
print(data[data['Survived'] == 0]['Age'].median())

# 9
print(data[data['Survived'] == 1]['Fare'].median())

# 10
print(data[data['Survived'] == 0]['Fare'].median())

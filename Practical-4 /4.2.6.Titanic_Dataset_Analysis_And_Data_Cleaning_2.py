#You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.

#code:

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1
data['IsAlone'] = np.where(data['FamilySize'] == 0, 1, 0)

# 2
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 4
print(data['Age'].mean())

# 5
print(data['Fare'].median())

# 6
print(data['Pclass'].value_counts())

# 7
print(data['Sex'].value_counts())

# 8
print(data['Survived'].value_counts())

# 9
print(data['Survived'].mean())

# 10
print(data.groupby('Sex')['Survived'].mean())

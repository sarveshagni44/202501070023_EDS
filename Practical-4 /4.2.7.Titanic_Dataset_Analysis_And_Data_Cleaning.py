#You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.

 code :

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

#1
print(data.groupby('Pclass')['Survived'].mean())

# 2
print(data.groupby('Embarked_S')['Survived'].mean())

# 3
print(data.groupby('FamilySize')['Survived'].mean())

# 4
print(data.groupby('IsAlone')['Survived'].mean())

# 5
print(data.groupby('Pclass')['Fare'].mean())

# 6
print(data.groupby('Pclass')['Age'].mean())

# 7
print(data.groupby('Survived')['Age'].mean())

# 8
print(data.groupby('Survived')['Fare'].mean())

# 9
print(data[data['Survived'] == 1]['Pclass'].value_counts())

# 10
print(data[data['Survived'] == 0]['Pclass'].value_counts())

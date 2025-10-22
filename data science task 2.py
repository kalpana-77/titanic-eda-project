import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\DELL\Downloads\The Titanic dataset.csv", skiprows=1)  # Skip first row with numbers

# Assign correct column names (10 columns)
data.columns = ['sn', 'pclass', 'survived', 'name', 'gender', 'age', 'family', 'fare', 'embarked', 'date']

print("Dataset loaded successfully!")
print(data.head())
print(data.info())

# Data Cleaning
print("\nMissing values before cleaning:")
print(data.isnull().sum())

# Convert data types
data['age'] = pd.to_numeric(data['age'], errors='coerce')
data['fare'] = pd.to_numeric(data['fare'], errors='coerce')
data['survived'] = pd.to_numeric(data['survived'], errors='coerce')
data['pclass'] = pd.to_numeric(data['pclass'], errors='coerce')

# Fill missing Age with median
data['age'].fillna(data['age'].median(), inplace=True)

# Fill missing Embarked with mode
data['embarked'].fillna(data['embarked'].mode()[0], inplace=True)

# Encode gender (male=0, female=1)
data['gender'] = data['gender'].map({'male': 0, 'female': 1})

# Drop rows with missing critical values
data.dropna(subset=['survived', 'pclass', 'gender'], inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

print("\nMissing values after cleaning:")
print(data.isnull().sum())
print(f"\nDataset shape after cleaning: {data.shape}")

# Exploratory Data Analysis (EDA)

# 1. Survival Count
plt.figure(figsize=(8, 6))
sns.countplot(x='survived', data=data)
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

# 2. Survival Rate by Gender
plt.figure(figsize=(8, 6))
sns.barplot(x='gender', y='survived', data=data)
plt.title('Survival Rate by Gender')
plt.xlabel('Gender (0 = Male, 1 = Female)')
plt.ylabel('Survival Rate')
plt.show()

# 3. Survival Rate by Passenger Class
plt.figure(figsize=(8, 6))
sns.barplot(x='pclass', y='survived', data=data)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# 4. Age Distribution by Survival
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', hue='survived', multiple='stack', bins=30)
plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 5. Fare Distribution by Survival
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='fare', hue='survived', multiple='stack', bins=30)
plt.title('Fare Distribution by Survival')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.xlim(0, 300)  # Limit x-axis for better visualization
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation_data = data[['survived', 'pclass', 'gender', 'age', 'family', 'fare']].corr()
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()

# 7. Survival by Class and Gender
plt.figure(figsize=(10, 6))
sns.barplot(x='pclass', y='survived', hue='gender', data=data)
plt.title('Survival Rate by Class and Gender')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.legend(title='Gender', labels=['Male', 'Female'])
plt.show()

# Summary Statistics
print("\n=== Summary Statistics ===")
print(f"Total passengers: {len(data)}")
print(f"Survival rate: {data['survived'].mean():.2%}")
print(f"\nSurvival by gender:")
print(data.groupby('gender')['survived'].mean())
print(f"\nSurvival by class:")
print(data.groupby('pclass')['survived'].mean())



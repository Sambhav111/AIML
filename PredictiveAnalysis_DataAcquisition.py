import pandas as pd

# Define the file path of the dataset
file_path = r'C:\Users\SAMBHAV SHARMA\OneDrive\Desktop\customer_churn.csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# Basic exploration of the data
print("First 5 rows of the dataset:")
print(df.head())  # Show first 5 rows

print("\nData Overview:")
print(df.info())  # Overview of columns, data types, and missing values

print("\nStatistical Summary:")
print(df.describe())  # Statistical summary for numerical columns

# Check for missing values in the dataset
print("\nMissing Values Count:")
print(df.isnull().sum())  # This will tell you the number of missing values per column

# Task 3: Pandas DataFrame Basics and Input/Output
# ============================================================

# This script demonstrates mastery of Pandas basics using the Superstore dataset.

# The script will:
# 1. Load the dataset into a DataFrame and inspect it
# 2. Filter rows and select specific columns
# 3. Create new calculated fields (e.g., profit margin)
# 4. Export subsets of the data to CSV files

import pandas as pd

#===========================================
# 1. Load the dataset
#===========================================
csv_file_path = "Sample - Superstore.csv"  # Dataset file in project folder
df = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding='latin-1')  # Load into DataFrame

# Display shape (rows x columns)
print("Dataset shape (rows x columns):", df.shape)

# Display column names
print("\nColumn names:", df.columns.tolist())

# Display data types for each column
print("\nColumn data types:")
print(df.dtypes)

# Show first 5 rows to verify data
print("\nTop 5 rows of dataset:")
print(df.head())

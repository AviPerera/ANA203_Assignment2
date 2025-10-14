# TASK 2: NumPy Arrays
# ===============================================================

# This task demonstrates how to use NumPy for efficient numeric analysis.
# It extracts sales, profit, and discount data from the Superstore dataset and performs statistical calculations using vectorised NumPy operations.
#

import numpy as np
import pandas as pd

# Load dataset
csv_file_path = "Sample - Superstore.csv"   # File must be in the same project folder
df = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding='latin-1')

print("\nDataset loaded successfully for NumPy analysis!")
print("=" * 50)

# ===============================================================
# 1: Extract numeric columns and convert them to NumPy arrays
# ===============================================================

# Extract sales, profit, and discount columns as numeric arrays
sales_array = df['Sales'].to_numpy()         # Converts pandas column to NumPy array
profit_array = df['Profit'].to_numpy()
discount_array = df['Discount'].to_numpy()

# Print data types to confirm they are NumPy arrays
print(f"Sales array type: {type(sales_array)}")
print(f"Profit array type: {type(profit_array)}")
print(f"Discount array type: {type(discount_array)}")
print("=" * 50)

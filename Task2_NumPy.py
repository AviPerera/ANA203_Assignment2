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

# ===============================================================
# 2: Perform vectorised statistical calculations
# ===============================================================

# Calculate mean (average)
mean_sales = np.mean(sales_array) # Average sales across all records
mean_profit = np.mean(profit_array)
mean_discount = np.mean(discount_array)

# Calculate median (middle value)
median_sales = np.median(sales_array)
median_profit = np.median(profit_array)

# Calculate standard deviation (measure of data spread)
std_sales = np.std(sales_array)
std_profit = np.std(profit_array)

# Print summary statistics
print("*** VECTORISED STATISTICAL CALCULATIONS ***")
print(f"Average Sales: ${mean_sales:.2f}")
print(f"Median Sales: ${median_sales:.2f}")
print(f"Sales Std. Deviation: ${std_sales:.2f}")
print(f"Average Profit: ${mean_profit:.2f}")
print(f"Profit Std. Deviation: ${std_profit:.2f}")
print(f"Average Discount: {mean_discount*100:.2f}%")
print("=" * 50)

# ===============================================================
# 3: Perform element wise operations
# ===============================================================
# NumPy allows performing arithmetic directly on arrays without loops

# Ex 1: Calculate profit-to-sales ratio for each record
profit_ratio = np.divide(profit_array, sales_array, out=np.zeros_like(profit_array), where=sales_array!=0)
# np.divide() divides each element of profit_array by sales_array safely (avoiding division by zero)

# Ex 2: Calculate discounted sales for each product
discounted_sales = sales_array * (1 - discount_array)

print("=== ELEMENT-WISE OPERATIONS EXAMPLES ===")
print("First 5 Profit Ratios (%):", np.round(profit_ratio[:5] * 100, 2))
print("First 5 Discounted Sales ($):", np.round(discounted_sales[:5], 2))
print("=" * 50)
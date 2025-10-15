# TASK 2: NumPy Arrays
# ===============================================================

# This task demonstrates how to use NumPy for efficient numeric analysis.
# It extracts sales, profit, and discount data from the Superstore dataset and performs statistical calculations using vectorised NumPy operations.
#


# This Demonstrates following concepts:
# - Creating and manipulating NumPy arrays
# - Performing mean, median, and standard deviation calculations
# - Applying element-wise operations
# - Demonstrating array slicing
# - Comparing NumPy performance with Python lists
#


# Real World Advantages of NumPy arrays:
# 1️. SPEED: NumPy arrays process large numeric data much faster than Python lists,
#    making it ideal for analytics on big datasets (e.g., thousands of sales records).
# 2️. VECTORIZATION: NumPy performs operations on entire arrays at once without loops,
#    which makes code simpler, cleaner, and less error-prone.
# ===============================================================

#Busniness Insights from Numpy

#Bisiness insight 1: Determining profitability trends and discount impact
# Insight 2: Identifying high-profit products and risk of low-profit items

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

# ===============================================================
# 4: Demonstrate array slicing
# ===============================================================
# Array slicing helps extract specific portions of an array efficiently

print("=== ARRAY SLICING EXAMPLES ===")
print("First 5 Sales Values:", sales_array[:5])     # First 5 elements
print("Every 10th Sale Record:", sales_array[::10])  # Every 10th element
print("Last 5 Profit Values:", profit_array[-5:])    # Last 5 elements
print("=" * 50)

# ===============================================================
# 5: Compare NumPy arrays with Python lists (Performance)
# ===============================================================
# This test shows how NumPy is faster than Python lists for large data.

import time

# Convert arrays to Python lists
sales_list = sales_array.tolist()

# Time how long it takes to sum all sales using Python list
start_time = time.time()
sum_sales_list = sum(sales_list)
list_time = time.time() - start_time

# Time how long it takes using NumPy
start_time = time.time()
sum_sales_numpy = np.sum(sales_array)
numpy_time = time.time() - start_time

print("*** PERFORMANCE COMPARISON ***")
print(f"Sum using Python list: ${sum_sales_list:.2f} (Time: {list_time:.6f} seconds)")
print(f"Sum using NumPy array: ${sum_sales_numpy:.2f} (Time: {numpy_time:.6f} seconds)")
print(f"NumPy is approximately {list_time / numpy_time:.2f}x faster!")
print("=" * 50)

# ===============================================================
# Business Insight Examples
# ===============================================================

# Bisiness insight 1: Determining profitability trends and discount impact
# ===============================================================

# Using NumPy results to generate a realworld insight for managers/ owners by calculating correlation between discounts and profits
correlation = np.corrcoef(discount_array, profit_array)[0, 1]

print("*** BUSINESS INSIGHTS: ")
print(f"Correlation between Discount and Profit: {correlation:.2f}")
if correlation < 0:
    print("Insight: Higher discounts tend to reduce profit margins.")
else:
    print("Insight: Discounts are positively influencing profit (unusual scenario).")
print("=" * 50)

# Bisiness insight 2: Identifying high-profit products and risk of low-profit items
# ===============================================================

# Using NumPy, we can find products that are consistently profitable and those that have very low or negative profits, helping managers make inventory and pricing decisions.

# Find the top 5 most profitable products (based on profit)
top_5_profit_indices = np.argsort(profit_array)[-5:]  # indices of 5 largest profits
top_5_profit_sales = sales_array[top_5_profit_indices]
top_5_profit = profit_array[top_5_profit_indices]

print("*** TOP 5 MOST PROFITABLE ORDERS ***")
for i in range(5):
    print(f"Order Index: {top_5_profit_indices[i]}, Sales: ${top_5_profit_sales[i]:.2f}, Profit: ${top_5_profit[i]:.2f}")
print("=" * 50)


# Find orders with negative profit
loss_indices = np.where(profit_array < 0)[0]  # indices where profit < 0
num_losses = len(loss_indices)
total_loss = profit_array[loss_indices].sum()



print("*** TOP NEGATIVE PROFIT ORDERS ***")
print(f"Number of orders with negative profit: {num_losses}")
print(f"Total loss from these orders: ${total_loss:.2f}")
print("Insight: Managers may review pricing, discounts, or suppliers for these orders.")
print("=" * 50)

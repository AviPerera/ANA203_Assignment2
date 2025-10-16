# TASK 2: NumPy Arrays
# ===============================================================

# Project: Comprehensive Exploratory Data Analysis of Superstore Sales Dataset
# Date: October 2025
# Unit: ANA203 Data Wrangling and Analysis with Python

# CODE REPOSITORY:
# Available on GitHub: https://github.com/AviPerera/ANA203_Assignment2
# Repository includes: Superstore dataset, 4 Task Files
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

#Busniness Insights using  Numpy

#   Business insight 1: Determining profitability trends and discount impact
#   Business Insight 2: Identifying high-profit products and risk of low profit items

import numpy as np
import pandas as pd


# Load CSV File
csv_file_path = "Sample - Superstore.csv"  # Load the Superstore dataset from the current project folder
github_url = "https://github.com/AviPerera/ANA203_Assignment2/blob/master/Sample%20-%20Superstore.csv"

try:
    # Using TRY block: Attempt to read the CSV file directly from the project root folder.
    # This works for:
    # - PyCharm (local project folder)
    # - Google Colab if the file has already been uploaded to the Colab root (/content)
    df = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding='latin-1')
    print("Dataset loaded from project root or Colab root.")

# If file is not found
except FileNotFoundError:
    # This block runs if the file wasn't found in the project root
    print("✗ File not found in project root. Checking alternative options...")

    try:
        # Option 2: Try Google Colab file upload
        # Import the files module from google.colab (only available in Colab environment)
        from google.colab import files

        # Tell the user to upload the file
        print("\n Please upload the CSV file...")
        # Open the file upload dialog in Colab and store uploaded files
        uploaded = files.upload()

        # Check if the correct filename was uploaded
        if csv_file_path in uploaded:
            # Load the uploaded file into a DataFrame with same parameters as before
            df = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding='latin-1')
            # Confirm successful upload and load
            print("Dataset loaded successfully from uploaded file.")
        else:
            # If wrong file was uploaded, raise an error
            raise FileNotFoundError(f"{csv_file_path} was not uploaded correctly.")

    except ImportError:
        # This runs if we're not in Colab (ImportError means google.colab doesn't exist)
        # Option 3: Load from GitHub if not in Colab
        print("Not running in Google Colab. Attempting to load from GitHub...")
        try:
            # Try to load the file directly from the GitHub URL
            df = pd.read_csv(github_url, on_bad_lines='skip', encoding='latin-1')
            # Confirm successful load from GitHub
            print("Dataset loaded successfully from GitHub repository.")
        except Exception as e:
            # If all three methods fail, raise a helpful error message
            raise FileNotFoundError(
                f"Could not load dataset from any source. Error: {str(e)}\n"
                f"Please ensure the file '{csv_file_path}' is in your project folder "
                f"or update the GitHub URL."
            )

# ============================================================================
# Data Profiling: Understanding the dataset
# ============================================================================

print("\n" + "="*50)
print("DATA PROFILING: INITIAL DATASET OVERVIEW")
print("="*80)

# Display basic dataset information
# df.shape[0] gives number of rows, df.shape[1] gives number of columns
print(f"\nDataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
# Calculate memory usage: memory_usage(deep=True) gives accurate memory
print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")


print("\n" + "-"*50)
print("Column Information:")
print("-"*80)

print(df.info())# df.info() shows column names, data types, non-null counts, and memory usage


print("\n" + "-"*50)
print("First 5 Rows (Sample Data):")
print("-"*80)

print(df.head())# df.head() displays the first 5 rows of the dataset so we can see what the data looks like


print("\n" + "-"*50)
print("Statistical Summary (Numerical Columns):")
print("-"*50)
# df.describe() provides count, mean, std, min, quartiles, and max for all numerical columns
print(df.describe())


print("\n" + "-"*50)
print("Missing Values Analysis:")
print("-"*50)
# Create a DataFrame to analyze missing values
missing_data = pd.DataFrame({
    'Column': df.columns,  # List all column names
    'Missing Count': df.isnull().sum(),  # Count how many missing values in each column
    'Missing %': (df.isnull().sum() / len(df) * 100).round(2)  # Calculate percentage of missing values
})
# Filter to only show columns that have missing values, sorted by most missing first
missing_data = missing_data[missing_data['Missing Count'] > 0].sort_values('Missing Count', ascending=False)

# Check if there are any missing values
if len(missing_data) > 0:
    print(missing_data.to_string(index=False))# If missing values exist, display the table without row index numbers
else:
    print("No missing values detected in the dataset.")



print("\n" + "-"*80)
print("Duplicate Rows Check:")
print("-"*80)
# Count how many rows are exact duplicates of other rows
duplicate_count = df.duplicated().sum()
# Check if duplicates exist
if duplicate_count > 0:
    # If duplicates found, show count and percentage
    print(f"Found {duplicate_count} duplicate rows ({duplicate_count/len(df)*100:.2f}%)")
else:
    print("No duplicate rows found.")


print("\nData Profiling Complete.")
print("="*80)

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

if numpy_time == 0:
    print("NumPy operation was too fast to measure accurately.")
else:
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

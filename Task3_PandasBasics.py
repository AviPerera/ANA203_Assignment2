# Task 3: Pandas DataFrame Basics and Input/Output
# ============================================================
# Project: Comprehensive Exploratory Data Analysis of Superstore Sales Dataset
# Date: October 2025
# Unit: ANA203 Data Wrangling and Analysis with Python

# CODE REPOSITORY:
# Available on GitHub: https://github.com/AviPerera/ANA203_Assignment2
# Repository includes: Superstore dataset, 4 Task Files


# This script demonstrates mastery of Pandas basics using the Superstore dataset.

# The script will:
# 1. Load the dataset into a DataFrame and inspect it
# 2. Filter rows and select specific columns
# 3. Create new calculated fields (e.g., profit margin)
# 4. Export subsets of the data to CSV files


#===========================================
#Real-world business scenarios where Pandas DataFrames are used
#===========================================

# Business Scenario 1: Sales Performance Analysis
#===========================================
# Objective: A retail chain wants to monitor which products, categories, or regions are generating the most sales and profit.

# Pandas Use:
  # Filter DataFrame for specific regions, products, or time periods.
  # Group by category, region, or customer segment to calculate total sales, average profit, or profit margins.
  # Sort and select top-performing products or stores.
  # Business Insight: Identify best-selling products and regions, plan inventory, marketing campaigns, and promotions accordingly.

# Business Scenario 2: Customer Segmentation
#===========================================

# Objective: A company wants to segment its customers by buying behavior, region, or total spending.

# Pandas Use:
  # Create new columns like total purchase per customer, average discount received, or number of orders.
  # Group by customer ID or segment.
  # Filter toptier customers (ex: Platinum members) for loyalty programs.
  # Business Insight: Target high-value customers with personalized offers, loyalty rewards, and retention campaigns.


import pandas as pd

#===========================================
# 1. Load the dataset
#===========================================

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

#===========================================
# 2. Filter rows and select columns
#===========================================

# Example: Filter orders from the 'West' region
west_region_orders = df[df['Region'] == 'West'].copy()  # Copy to avoid SettingWithCopyWarning
print("\nNumber of orders from West region:", len(west_region_orders))

# Select only relevant columns for analysis
west_region_orders_subset = west_region_orders[['Order ID', 'Customer Name', 'Category', 'Sales', 'Profit', 'Quantity']]
print("\nSample orders from West region:")
print(west_region_orders_subset.head())

#===========================================
# 3. Create calculated fields
#===========================================

# Profit Margin = Profit / Sales * 100
# Using vectorised Pandas operations for efficiency
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

# Display first 5 rows with new column
print("\nDataset with Profit Margin column:")
print(df[['Order ID', 'Sales', 'Profit', 'Profit Margin (%)']].head())

# Example: Average profit margin by Category
avg_profit_margin = df.groupby('Category')['Profit Margin (%)'].mean()
print("\nAverage Profit Margin by Category:")
print(avg_profit_margin)

#===========================================
# 4. Export subsets to CSV
#===========================================

# Export all orders from 'Technology' category
technology_orders = df[df['Category'] == 'Technology'].copy()
technology_orders.to_csv("technology_orders.csv", index=False)
print("\nSaved Technology category orders to 'technology_orders.csv'")

# Export high-profit orders (profit > $500)
high_profit_orders = df[df['Profit'] > 500].copy()
high_profit_orders.to_csv("high_profit_orders.csv", index=False)
print("Saved high-profit orders to 'high_profit_orders.csv'")

#===========================================
# 5. Demonstrate selecting specific rows and columns
#===========================================

# First 10 orders with highest sales
top_sales_orders = df.nlargest(10, 'Sales')[['Order ID', 'Customer Name', 'Sales', 'Profit']]
print("\nTop 10 orders by Sales:")
print(top_sales_orders)

#===========================================
# 6. Export filtered subset for review
#===========================================

# Example: Export West region subset
west_region_orders_subset.to_csv("west_region_orders.csv", index=False)
print("Saved West region orders to 'west_region_orders.csv'")

print("\n Basic Pandas DataFrame operations completed successfully!")

#===========================================
#Real world business scenarios where Pandas DataFrames are used
#===========================================


#===========================================
# Scenario 1: Sales Performance Analysis
#===========================================
# Objective: Find total sales and average profit by Category and Region

# Group the data by 'Category' and 'Region', calculate total sales and average profit
sales_perf = df.groupby(['Category', 'Region']).agg(
    total_sales=pd.NamedAgg(column='Sales', aggfunc='sum'),       # Sum of Sales per group
    average_profit=pd.NamedAgg(column='Profit', aggfunc='mean')   # Average Profit per group
).reset_index()  # Reset index to turn groupby object into DataFrame

# Sort by total_sales descending for better insight
sales_perf = sales_perf.sort_values(by='total_sales', ascending=False)

# Display the result
print("*** Scenario 1: Sales Performance Analysis ***")
print(sales_perf.head(10))  # Show top 10 Category-Region combinations
print("="*50)

#===========================================
# Scenario 2: Customer Segmentation
#===========================================
# Objective: Segment customers by total spending and number of orders

# Calculate total spending and total number of orders per customer
customer_segment = df.groupby(['Customer ID', 'Customer Name']).agg(
    total_spent=pd.NamedAgg(column='Sales', aggfunc='sum'),      # Sum of sales per customer
    total_orders=pd.NamedAgg(column='Order ID', aggfunc='nunique')  # Count unique orders per customer
).reset_index()

# segment customers into tiers based on total spending
# Here we define 3 tiers: High (> $5000), Medium ($2000-$5000), Low (< $2000)
def assign_tier(spent):
    if spent > 5000:
        return "High"
    elif spent >= 2000:
        return "Medium"
    else:
        return "Low"

customer_segment['Tier'] = customer_segment['total_spent'].apply(assign_tier)  # Apply tier assignment

# Sort customers by total spending descending
customer_segment = customer_segment.sort_values(by='total_spent', ascending=False)

# Display the top 10 customers
print("*** Scenario 2: Customer Segmentation ***")
print(customer_segment.head(10))
print("="*50)
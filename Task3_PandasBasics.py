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
#Real-world business scenarios where Pandas DataFrames are used
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
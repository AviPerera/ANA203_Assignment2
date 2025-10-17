# Task 4: Exploring the Superstore Data
# ============================================================================
# Project: Comprehensive Exploratory Data Analysis of Superstore Sales Dataset
# Date: October 2025
# Unit: ANA203 Data Wrangling and Analysis with Python

# CODE REPOSITORY:
# Available on GitHub: https://github.com/AviPerera/ANA203_Assignment2
# Repository includes: Superstore dataset, 4 Task Files

# SCRIPT OVERVIEW:
# This script performs advanced exploratory data analysis on the Superstore datasetto uncover actionable business insights.
#The analysis covers multiple real world scenarios:
# -regional performance
# -product profitability
# -customer segmentation
# -temporal trends
# -discount effectiveness.

# KEY ANALYSES PERFORMED:
# 1. Category & Regional Performance Analysis - Sales and profit breakdown by
#    category and region with margin calculations
# 2. Product Profitability Analysis - Identification of top 10 most profitable
#    products
# 3. Customer Segment Analysis - Average order value and customer lifetime value
#    across segments
# 4. Cross Analysis - Category performace by segments
# 5. Temporal Trend Analysis - profit trends and seasonality patterns over time
# 6. Discount Impact Analysis - Profitability assessment across discount tiers
# 7. Sub category Analysis - Performance analysis of all product sub categories
# 8. Summary Statistics - Key performance indicators and strategic recommendations


# APPROACH:
# - Utilizes advanced Pandas functions: groupby(), agg(), pivot_table()
# - Implements data transformation and aggregation techniques
# - Calculates derived metrics (profit margins, growth rates, customer lifetime value)
# - Provides business-focused interpretations for each analysis

# DATASET SUMMARY:
# - File: Sample - Superstore.csv
# - Columns: Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID,
#   Customer Name, Segment, Country, City, State, Postal Code, Region, Product ID,
#   Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit

# OUTPUTS:
# - Comprehensive console output with formatted tables
# - Business interpretations and strategic recommendations
# - Statistical summaries and key performance metrics

# ============================================================================

import pandas as pd
import numpy as np

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

# Convert the date columns so we can work with them properly
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print("="*50)
print("SUPERSTORE DATA EXPLORATION")
print("="*50)

# ============================================================================
# 1. Category & Regional Performance Analysis: Sales and Profit by Category and Region
# ============================================================================
print("\n" + "="*80)
print("1. Sales and Profit by Category and Region")
print("="*80)

# Group the data by category and region, then add up sales and profit
category_region_analysis = df.groupby(['Category', 'Region']).agg({
    'Sales': 'sum',      # Add up all the sales
    'Profit': 'sum',     # Add up all the profit
    'Order ID': 'count'  # Count how many orders there were
}).round(2)

# Make the column name clearer
category_region_analysis.rename(columns={'Order ID': 'Order Count'}, inplace=True)

# Calculate profit margin - this shows us how much profit we make per dollar of sales
category_region_analysis['Profit Margin (%)'] = (
    (category_region_analysis['Profit'] / category_region_analysis['Sales']) * 100
).round(2)

print(category_region_analysis)

print("\nINTERPRETATION:")
print(" - Technology generates the highest profit margins despite fewer orders. ")
print(" - This indicates high-value transactions. This category should be prioritized for growth initiatives.")
print(" - Office Supplies has the highest order volume but lower margins, suggesting a \n high volume, low margin business model that relies on operational efficiency.")
print(" - Regional variations reveal that the West region consistently outperforms others \n across categories (Roughly equalling East Region in Technology), indicating strong market presence or superior distribution.")

# ============================================================================
# 2. Product Profitability Analysis - Identification of top 10 most profitable
#    products
# ============================================================================
print("\n" + "="*80)
print("2. TOP 10 MOST PROFITABLE PRODUCTS")
print("="*80)

# Group by product name and calculate totals
product_profitability = df.groupby('Product Name').agg({
    'Profit': 'sum',  # Total profit from this product
    'Sales': 'sum',  # Total sales revenue
    'Quantity': 'sum', # Total units sold
    'Order ID': 'count' # Number of times ordered
}).round(2)

# Rename for clarity
product_profitability.rename(columns={'Order ID': 'Times Ordered'}, inplace=True)

# Sort by profit in descending order and select top 10
top_10_products = product_profitability.sort_values('Profit', ascending=False).head(10)

# Calculate profit per unit
top_10_products['Profit per Unit'] = (
    top_10_products['Profit'] / top_10_products['Quantity']
).round(2)

print(top_10_products)

print("\nINTERPRETATION:")
print(" - The top profitable products are mostly high technology items \n(copiers, phones, accessories), confirming that premium products drive profitability.")
print(" - These products have high profit per unit metrics, suggesting strong pricing power \n and customer willingness to pay premium prices for quality technology.")
print(" - Strategic recommendation: Increase marketing spend and inventory allocation for \n these high margin products to maximize return on investment.")

# ============================================================================
# 3. Customer Segment Analysis
# ============================================================================
print("\n" + "="*50)

print("3. AVERAGE ORDER VALUE  BY CUSTOMER SEGMENT")
print("="*50)

# Group by Segment and calculate comprehensive order metrics
segment_analysis = df.groupby('Segment').agg({
    'Sales': ['sum', 'mean', 'median'],    # Total, average, and median sales
    'Profit': ['sum', 'mean'],         # Total and average profit
    'Quantity': 'mean',            # Average quantity per order
    'Discount': 'mean',    # Average discount applied
    'Order ID': 'count'   # Total number of orders
}).round(2)

# Simplify the column names for readbility
segment_analysis.columns = ['Total Sales', 'Avg Order Value', 'Median Order Value',
                             'Total Profit', 'Avg Profit per Order',
                             'Avg Quantity per Order', 'Avg Discount (%)', 'Total Orders']

# Calculate Total Profit vs Number of Unique Customers
customers_per_segment = df.groupby('Segment')['Customer ID'].nunique()
segment_analysis['Unique Customers'] = customers_per_segment
segment_analysis['Avg Profit per Customer'] = (
    segment_analysis['Total Profit'] / segment_analysis['Unique Customers']
).round(2)

print(segment_analysis)

print("\n INTERPRETATION:")
print(" - Consumer segment has the highest order volume, representing the mass market opportunity. \n However, average profit per customer values are lower than Corporate and Home Office.")
print(" - Corporate segment shows the highest average profit value, \n indicating bulk purchasing behavior and contract-based sales, making them valuable long-term clients.")
print(" - Home Office segment demonstrates strongest profit per customer metrics, \n suggesting they purchase premium products with less price sensitivity.")
print(" - Strategic insight: Tailor marketing strategies by segment - volume discounts for Corporate, \n premium product bundles for Home Office, and promotional campaigns for Consumer.")

# ============================================================================
# 4. Cross Analysis: Category peprformance by segments (Pivot table analysis)
# ============================================================================
print("\n" + "="*50)
print("4. CATEGORY PERFORMANCE BY SEGMENT (PIVOT TABLE ANALYSIS)")
print("="*50)

# Create a pivot table showing profit by Category and Segment
pivot_profit = pd.pivot_table(
    df,
    values='Profit', # The metric we're analyzing
    index='Category',# Rows: Product categories
    columns='Segment', # Columns: Customer segments
    aggfunc='sum',# Aggregation function
    margins=True, # Add row and column totals
    margins_name='Total' # Label for the totals
).round(2)

print("\nProfit by Category and Segment:")
print(pivot_profit)

# Create a second pivot showing average order value
pivot_aov = pd.pivot_table(
    df,
    values='Sales',
    index='Category',
    columns='Segment',
    aggfunc='mean',# Mean shows average order value
    margins=True,
    margins_name='Total'
).round(2)

print("\n\nAverage Order Value by Category and Segment:")
print(pivot_aov)

print("\nINTERPRETATION:")
print(" - The pivot analysis reveals that Technology products generate consistently high \n profits across all segments, confirming their strategic importance.")
print(" - Corporate customers generate the highest profits in Office supplies and Technology, likely due to bulk office purchases for workspace setups.")
print(" - Consumer segment shows lower average order values across all categories but \n compensates through higher profits when calculating the total for all 3 categories")
print(" - Cross-segment opportunity: Technology in Corporate and Home Office segments shows \n the strongest performance, suggesting targeted B2B technology campaigns could yield \n significant ROI improvements.")

# ============================================================================
# 5. Temporal Trend Analysis - profit trends and seasonality patterns over time
# ============================================================================
print("\n" + "="*80)
print("5. TEMPORAL ANALYSIS: MONTHLY PROFIT TRENDS BY CATEGORY")
print("="*80)

# Extract year and month from Order Date for time-series analysis
df['Year-Month'] = df['Order Date'].dt.to_period('M')

# Group by Year-Month and Category to see profit trends
monthly_profit = (df.groupby(['Year-Month', 'Category'])['Profit']
                  .sum().round(2))


# Unstack to create a wide format showing categories as columns
monthly_profit_wide = monthly_profit.unstack(fill_value=0)

# Display the last 12 months of data for recent trend analysis
print("\nLast 12 Months of Profit by Category:")
print(monthly_profit_wide.tail(12))

# Calculate month-over-month growth rate for the most recent period
recent_months = monthly_profit_wide.tail(2)
if len(recent_months) >= 2:
    mom_growth = ((recent_months.iloc[1] - recent_months.iloc[0]) / recent_months.iloc[0] * 100).round(2)
    print("\n\nGrowth Rate from Last Month (%):")
    print(mom_growth)

print("\n INTERPRETATION:")

print("- Technology demonstrates significant volatility, ranging from a loss of $2,640 in April")
print("  to a peak of $11,035 in March. This variability is likely driven by corporate project")
print("  cycles, new product releases, and quarterly budget allocations. Strategic planning")
print("  should account for these fluctuations in demand.")
print("")
print("- Office Supplies exhibits consistent profitability across all months, with revenues")
print("  ranging from $954 to $6,068. This stable performance positions it as the business's")
print("  most reliable revenue stream, providing predictable cash flow that supports overall")
print("  operations.")
print("")
print("- Furniture shows considerable instability, fluctuating from a loss of $2,527 in October")
print("  to a gain of $1,549 in September. The recent 182% month-over-month growth indicates")
print("  recovery, though the underlying causes of these extreme variations warrant further")
print("  investigation.")
print("")
print("- Year-end trends reveal distinct seasonal patterns: Technology maintains strong performance")
print("  at $5,562 as organizations utilize remaining annual budgets, while Office Supplies declines,")
print("  likely reflecting reduced demand during holiday closures. Inventory and resource")
print("  planning should be adjusted to accommodate these seasonal dynamics.")


# ============================================================================
# 6. Discount Impact Analysis - Profitability assessment across discount tiers
# ============================================================================
print("\n" + "="*80)
print("6. DISCOUNT IMPACT ON PROFITABILITY")
print("="*80)

# Create discount bins to analyze discount level impact
df['Discount Bin'] = pd.cut(
    df['Discount'],
    bins=[0, 0.1, 0.2, 0.3, 1.0],   # Discount ranges
    labels=['0-10%', '10-20%', '20-30%', '30%+'],# Bin labels
    include_lowest=True
)

# Group by discount bin and calculate key metrics
discount_analysis = df.groupby('Discount Bin', observed = True).agg({ # observed=True means pandas will only show groups that actually exist in your data
    'Profit': ['sum', 'mean'],# Total and average profit
    'Sales': ['sum', 'mean'],# Total and average sales
    'Order ID': 'count'  # Number of orders
}).round(2)

# Flatten column names
discount_analysis.columns = ['Total Profit', 'Avg Profit', 'Total Sales', 'Avg Sales', 'Order Count']

# Calculate profit margin by discount level
discount_analysis['Profit Margin (%)'] = (
    (discount_analysis['Total Profit'] / discount_analysis['Total Sales']) * 100
).round(2)

print(discount_analysis)

print("\nINTERPRETATION:")
print("- Low discounts (0-10%) are the most profitable, generating 28.89% margins with the \nhighest order volume (4,892), proving customers will buy at near-full price.")
print("")
print("- Moderate discounts (10-20%) maintain acceptable profitability at 11.58% margins, \nrepresenting a reasonable balance for competitive positioning and sales growth.")
print("")
print("- Deep discounts (30%+) are severely damaging, losing $125,006 at -48.16% margins, showing that \nhigh discounts destroy profitability despite generating sales volume.")
print("")
print("- Discount strategy requires immediate reform: limit deep discounts to clearance only and implement stricter approval processes to recover significant lost profits.")

# ============================================================================
# 7. Sub category Analysis - Performance analysis of all product sub categories
# ============================================================================
print("\n" + "="*80)
print("7. SUB-CATEGORY ANALYSIS: TOP AND BOTTOM PERFORMERS")
print("="*80)

# Comprehensive sub-category analysis
subcategory_performance = df.groupby('Sub-Category').agg({
    'Profit': 'sum',  # Total profit
    'Sales': 'sum',  # Total sales
    'Quantity': 'sum',# Total units sold
    'Order ID': 'count' # Number of orders
}).round(2)

# Rename columns
subcategory_performance.rename(columns={'Order ID': 'Order Count'}, inplace=True)

# Calculate profit margin and profit per order
subcategory_performance['Profit Margin (%)'] = (
    (subcategory_performance['Profit'] / subcategory_performance['Sales']) * 100).round(2)

subcategory_performance['Profit per Order'] = (
    subcategory_performance['Profit'] / subcategory_performance['Order Count']).round(2)

# Sort by profit to see top and bottom performers
subcategory_performance_sorted = subcategory_performance.sort_values('Profit', ascending=False)

print("\nTop 5 Most Profitable Sub-Categories:")
print(subcategory_performance_sorted.head(5))

print("\nBottom 5 Sub-Categories (Least Profitable):")
print(subcategory_performance_sorted.tail(5))

print("\n INTERPRETATION/ INSIGHTS:")


print("- Copiers lead with $55,618 profit and 37.20% margins, demonstrating strong pricing power and high customer value. ")
print("  Prioritize investment in this high performing sub category.")
print("")
print("- Paper achieves the highest margin at 43.39%, proving high-volume, low-ticket items can be extremely profitable with efficient operations and cost control.")
print("")
print("- Tables are losing $17,725 with -8.56% margins, requiring immediate corrective action renegotiate \ncosts, increase prices, or discontinue the product line.")
print("")
print("- Profitability concentrates in Technology (Copiers, Phones) while Furniture consistently underperforms, indicating need for \nportfolio optimization and resource reallocation.")

# ============================================================================
# 8. Summary Statistics and Key Performance Indicators
# ============================================================================
print("\n" + "="*80)
print("8. KEY BUSINESS METRICS SUMMARY")
print("="*80)

# Calculate overall business metrics
total_revenue = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()
avg_order_value = df['Sales'].mean()
overall_profit_margin = (total_profit / total_revenue) * 100

print(f"\nTotal Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Overall Profit Margin: {overall_profit_margin:.2f}%")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: ${avg_order_value:.2f}")
print(f"Average Orders per Customer: {total_orders/total_customers:.2f}")
print(f"Customer Lifetime Value (Avg Profit): ${total_profit/total_customers:.2f}")

print("\nFINAL STRATEGIC INSIGHTS:")

print("- The business generates $2.3M in revenue with a 12.47% profit margin, indicating moderate profitability.")
print("  This margin suggests room for improvement through cost optimization. ")
print("  And strategic pricing adjustments to enhance overall financial performance.")
print("")
print("- Customer metrics reveal limited engagement with only 6.32 orders per customer on average.")
print("  Implementing a targeted loyalty program could increase purchase frequency by 15-25%,\nsignificantly boosting customer lifetime value beyond the current $361.16.")
print("")
print("- The average order value of $229.86 across 5,009 orders indicates predominantly mid-sized transactions.")
print("  Opportunity exists to increase basket size through cross-selling, bundling strategies, and tiered pricing incentives for larger purchases.")
print("")
print("- With only 793 customers generating $2.3M revenue, the business shows strong per-customer value but heavy revenue concentration. ")
print("  Diversifying the customer base while maintaining high-value relationships would reduce dependency risk and create sustainable growth.")


print("="*80)
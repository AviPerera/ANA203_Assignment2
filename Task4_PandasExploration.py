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

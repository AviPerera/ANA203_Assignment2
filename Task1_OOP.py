# Task 1: Object Oriented Programming
# =============================================

# Project: Comprehensive Exploratory Data Analysis of Superstore Sales Dataset
# Date: October 2025
# Unit: ANA203 Data Wrangling and Analysis with Python

# CODE REPOSITORY:
# Available on GitHub: https://github.com/AviPerera/ANA203_Assignment2
# Repository includes: Superstore dataset, 4 Task Files

# DATASET SUMMARY:
# - File: Sample - Superstore.csv
# - Columns: Row ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID,
#   Customer Name, Segment, Country, City, State, Postal Code, Region, Product ID,
#   Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit

# SCRIPT OVERVIEW:
# =============================================
# This script demonstrates OOP concepts (Abstraction, Encapsulation, Inheritance, Polymorphism)
# using the Superstore dataset. It models real-world business entities such as Customer, Product, Order, Category, and Shipment.
# And use those concepts to seamlessly model real world busness scenarios

# OOP concepts demonstrated in this script:
# *******************************************

# ABSTRACTION
# ==================
# Abstraction means hiding complex details and showing only necessary information.
# For example, when creating a Customer object, we don’t need to know how it stores or calculates data.
# We just use its methods like get_customer_info().

# ENCAPSULATION
# =================
# Encapsulation means keeping data safe by restricting direct access.
# We use private variables (with underscores like _name) and public methods to access them safely.

# INHERITANCE
# =================
# Inheritance means one class can reuse or extend another.
# For example, both Category and Product can share common properties like name and ID.

# POLYMORPHISM
# =================
# Polymorphism means that methods with the same name can behave differently for different classes.
# Example: The show_info() method is defined differently in several classes.

# Example business scenarios demonstrated in this script:
# *******************************************************


# Scenario 1: Customer Order Summary and Profit Analysis
# ----------------------------------------------------------
# In this scenario, the system creates several Customer, Product, and Order objects using data from the Superstore dataset.
# It demonstrates how an Order object links Customer and Product classes through inheritance and composition.
# The program calculates each order’s total sales, discount, and profit margin, then prints a readable summary for managers to quickly review sales performance.
#
# Demonstrated OOP Concepts:
# - Abstraction: Hiding internal calculations in methods (ex: discounted_total()).
# - Encapsulation: Controlled access to Customer data through getter methods.
# - Inheritance: Order inherits from Product to reuse its attributes and methods.
# - Polymorphism: show_info() behaves differently in multiple classes.
#
# Scenario 2: Regional Sales and Shipping Efficiency Report
# ----------------------------------------------------------
# This scenario simulates a regional sales analysis where the system groups orders by customer region and calculates the total number of orders, sales revenue, and average shipping delay per region.
# It uses multiple objects (Customer, Order, Shipment) working together to provide a practical business insight helping management identify which regions perform best and whether certain shipping modes are slower or less efficient.
#
# Demonstrated OOP Concepts:
# - Reusability: Using existing classes to build new analytics without rewriting logic.
# - Abstraction: Hiding data manipulation logic inside methods (ex: class methods for counting).
# - Polymorphism: Using the same show_info() method across different entity types.
# - Composition: Combining multiple objects (Customer + Shipment + Order) to model realworld data.
# ==========================================================


# import  required libraries
import pandas as pd
import re

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

# ======================================================
# Class 1: Customer
# Demonstrates Encapsulation and Abstraction
# ======================================================

class Customer:
    def __init__(self, customer_id, customer_name, region):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.region = region

    def get_customer_name(self):  # Getter method to access private attribute (Encapsulation)
        return self.customer_name

    def get_region(self):
        return self.region

    # Example of abstraction: hiding how info is formatted
    def get_customer_info(self):
        return f"{self.customer_name} (ID: {self.customer_id}) - Region: {self.region}"
        # Returns formatted customer info without shouwing how it's constructed

    # Example of a class method: counts total unique customers
    @classmethod
    def count_customers(cls, dataframe):  # Uses pandas to count unique Customer IDs in the dataset
        return dataframe["Customer ID"].nunique()

    @staticmethod
    def validate_customer_id(customer_id):
        """
        Validates that the customer ID follows the format 'AA-12345'
          - Starts with two uppercase letters
          - Followed by a hyphen '-'
          - Followed by exactly 5 digits
        """
        pattern = r"^[A-Z]{2}-\d{5}$"
        return bool(re.match(pattern, customer_id))


# ======================================================
# CLASS 2: Category
# Demonstrates simple data grouping
# ======================================================
class Category:
    def __init__(self, category_name, sub_category):  # Store category and sub-category names

        self.category_name = category_name
        self.sub_category = sub_category

    def show_info(self):
        # Returns formatted category info
        return f"Category: {self.category_name} | Sub-category: {self.sub_category}"


# ======================================================
# CLASS 3: Product
# Demonstrates Constructors, Instance Methods, and Abstraction
# ======================================================
class Product:
    # Store key attributes about the product
    def __init__(self, product_id, category, sub_category, name, sales, quantity, discount, profit):
        self.product_id = product_id
        self.category = category
        self.sub_category = sub_category
        self.name = name
        self.sales = sales
        self.quantity = quantity
        self.discount = discount
        self.profit = profit

    def total_sales(self):
        # Calculates total sales value
        return self.sales * self.quantity

    def profit_margin(self):
        # Calculates profit percentage safely
        return (self.profit / self.sales) * 100 if self.sales > 0 else 0

    def show_info(self):
        # Polymorphism: similar method name used in other classes but with different meaning
        return f"Product: {self.name} | Sales: ${self.sales:.2f} | Profit Margin: {self.profit_margin():.2f}%"


# ======================================================
# CLASS 4: Shipment
# Demonstrates basic data representation and Abstraction
# ======================================================

class Shipment:
    def __init__(self, ship_mode, ship_date, city):
        # Store delivery information
        self.ship_mode = ship_mode
        self.ship_date = ship_date
        self.city = city

    def show_info(self):
        # Returns formatted delivery information
        return f"Shipped via {self.ship_mode} to {self.city} on {self.ship_date}"


# ======================================================
# CLASS 5: Order (inherits from Product)
# Demonstrates Inheritance and Polymorphism

# ======================================================

class Order(Product):
    def __init__(self, order_id, order_date, customer: Customer, product_id, category, sub_category,
                 name, sales, quantity, discount, profit):
        # Reuse attributes from Product using inheritance
        super().__init__(product_id, category, sub_category, name, sales, quantity, discount, profit)
        # Add orderspecific attributes
        self.order_id = order_id
        self.order_date = order_date
        self.customer = customer

    def discounted_total(self):
        # Abstraction: hides formula logic, just gives result
        return self.sales * self.quantity * (1 - self.discount)

    def total_sales(self):
        # Polymorphism: overrides total_sales() method in Product
        return self.sales * self.quantity * (1 - self.discount)

    def order_summary(self):
        # Returns full order summary
        return (f"Order ID: {self.order_id} | Customer: {self.customer.get_customer_name()} | "
                f"Product: {self.name} | Total after discount: ${self.total_sales():.2f}")

    @classmethod
    def from_dataset(cls, row):
        # Creates customer automatically from dataset row
        customer = Customer(row['Customer ID'], row['Customer Name'], row['Region'])
        # Create order using dataset info
        return cls(row['Order ID'], row['Order Date'], customer,
                   row['Product ID'], row['Category'], row['Sub-Category'],
                   row['Product Name'], row['Sales'], row['Quantity'],
                   row['Discount'], row['Profit'])


# ==================================
# CREATE OBJECTS FROM EACH CLASS
# ==================================

# Take first row from dataset as sample
row = df.iloc[0]

# Create Customer object
# ------------------------
customer1 = Customer(row['Customer ID'], row['Customer Name'], row['Region'])
print("\n Customer Info:", customer1.get_customer_info())

# Create Category object
# ------------------------
category1 = Category(row['Category'], row['Sub-Category'])
print(" Category Info:", category1.show_info())

# Create Product object
# ------------------------
product1 = Product(row['Product ID'], row['Category'], row['Sub-Category'],
                   row['Product Name'], row['Sales'], row['Quantity'],
                   row['Discount'], row['Profit'])
print(" Product Info:", product1.show_info())

# Create Shipment object
# ------------------------
shipment1 = Shipment(row['Ship Mode'], row['Ship Date'], row['City'])
print(" Shipment Info:", shipment1.show_info())

# Create Order object using from_dataset class method
order1 = Order.from_dataset(row)
print(" Order Summary:", order1.order_summary())

# Demonstrate class and static methods
print("\n Total unique customers in dataset:", Customer.count_customers(df))
print(" Is customer ID valid?", Customer.validate_customer_id(customer1.customer_id))

# ======================================================
# BUSINESS SCENARIOS
# ======================================================


print("BUSINESS SCENARIO 1: PRODUCT PERFOMANCE ANALYSIS")

# ==========================================================
# BUSINESS SCENARIO 1: Customer Order Summary and Profit Analysis
# ==========================================================


def create_customer_orders(dataframe):
    """Creates and returns a list of Order objects with linked Customer and Product details."""
    orders = []

    # Use the first 5 rows to create sample orders for demonstration
    for _, row in dataframe.head(5).iterrows():
        # Create a Customer object
        customer = Customer(row['Customer ID'], row['Customer Name'], row['Region'])

        # Create an Order object using inherited Product attributes
        order = Order(
            order_id=row['Order ID'],
            order_date=row['Order Date'],
            customer=customer,
            product_id=row['Product ID'],
            category=row['Category'],
            sub_category=row['Sub-Category'],
            name=row['Product Name'],
            sales=row['Sales'],
            quantity=row['Quantity'],
            discount=row['Discount'],
            profit=row['Profit']
        )

        # Add the new order to the list
        orders.append(order)

    return orders


def display_order_summaries(orders):
    """Prints a summary of each order, showing customer info, sales, discount, and profit margin."""
    print("\n*** CUSTOMER ORDER SUMMARY AND PROFIT ANALYSIS ***\n")

    total_sales = 0
    total_profit = 0

    # Loop through each order object
    for order in orders:
        # Print readable summary for each order
        print(f"Order ID: {order.order_id}")
        print(f"Customer: {order.customer.get_customer_info()}")  # Uses encapsulated getter
        print(f"Product: {order.name} ({order.category} - {order.sub_category})")
        print(f"Quantity: {order.quantity}")
        print(f"Sales (before discount): ${order.sales * order.quantity:.2f}")
        print(f"Discount Applied: {order.discount * 100:.0f}%")
        print(f"Final Total (after discount): ${order.discounted_total():.2f}")
        print(f"Profit Margin: {order.profit_margin():.2f}%")
        print("-" * 80)

        # Keep running totals for business reporting
        total_sales += order.discounted_total()
        total_profit += order.profit

    # Display overall totals
    print("\n *** OVERALL BUSINESS PERFORMANCE ***")
    print(f"Total Orders: {len(orders)}")
    print(f"Total Sales (after discount): ${total_sales:.2f}")
    print(f"Total Profit: ${total_profit:.2f}")
    print(f"Average Profit Margin: {(total_profit / total_sales) * 100:.2f}%")
    print("====================================================================\n")


# RUN THE SCENARIO ==============
print("\n--- Running Scenario 1: Customer Order Summary and Profit Analysis ---")

# Create Customer and Order objects from dataset
customer_orders = create_customer_orders(df)

# Display summaries for all created orders
display_order_summaries(customer_orders)

# ==========================================================
# SCENARIO 2: Regional Sales and Shipping Efficiency Report
# ==========================================================

import datetime


# Function to simulate creation of Order and Shipment objects from a few dataset rows
def create_sample_orders(dataframe):
    """Creates a list of Order objects using sample rows from the dataset."""
    sample_orders = []

    # Take only the first 10 rows for demonstration purposes
    for _, row in dataframe.head(10).iterrows():
        # Create a Customer object
        customer = Customer(row["Customer ID"], row["Customer Name"], row["Region"])

        # Create a Shipment object
        shipment = Shipment(row["Ship Mode"], row["Ship Date"], row["City"])

        # Create an Order object (inherits Product details)
        order = Order(
            order_id=row["Order ID"],
            order_date=row["Order Date"],
            customer=customer,
            product_id=row["Product ID"],
            category=row["Category"],
            sub_category=row["Sub-Category"],
            name=row["Product Name"],
            sales=row["Sales"],
            quantity=row["Quantity"],
            discount=row["Discount"],
            profit=row["Profit"]
        )

        # Attach shipment to the order (composition relationship)
        order.shipment = shipment

        # Add to the list
        sample_orders.append(order)

    return sample_orders


# Function to calculate regional performance
def analyse_regional_sales(orders):
    """Groups orders by region and calculates key metrics (total sales, order count, average shipping delay)."""

    region_data = {}

    for order in orders:
        region = order.customer.get_region()  # Get region from Customer object
        ship_date = pd.to_datetime(order.shipment.ship_date)
        order_date = pd.to_datetime(order.order_date)

        # Calculate shipping delay in days
        shipping_delay = (ship_date - order_date).days

        # Add region data if not already
        if region not in region_data:
            region_data[region] = {
                "total_sales": 0,
                "order_count": 0,
                "total_shipping_delay": 0
            }

        # Update metrics for the region
        region_data[region]["total_sales"] += order.total_sales()
        region_data[region]["order_count"] += 1
        region_data[region]["total_shipping_delay"] += shipping_delay

    # Print region-wise summary
    print("\n *** REGIONAL SALES AND SHIPPING EFFICIENCY REPORT ***\n")
    print("*" * 50)
    for region, stats in region_data.items():
        avg_delay = stats["total_shipping_delay"] / stats["order_count"]
        print(f"Region: {region}")
        print(f"  Total Orders: {stats['order_count']}")
        print(f"  Total Sales: ${stats['total_sales']:.2f}")
        print(f"  Average Shipping Delay: {avg_delay:.1f} days")
        print("-" * 55)


# ============= RUN THE SCENARIO ==============
print("\n\n--- Running Scenario 2: Regional Sales and Shipping Efficiency Report ---")

# Create a few sample order objects
orders_list = create_sample_orders(df)

# Display details of the first few orders to show polymorphism (same show_info() name used in Shipment & Order)
print("\nSample Order Details:\n")
for order in orders_list[:3]:
    print(order.order_summary())  # From Order class
    print(order.shipment.show_info())  # From Shipment class
    print("-" * 50)

# Analyse and display region-wise performance
analyse_regional_sales(orders_list)

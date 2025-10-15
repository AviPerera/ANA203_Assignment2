# Task 1: Object Oriented Programming

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

# Example busness scenarios demonstrated in this script:
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


# import  required libararies
import pandas as pd
import re

# Load CSV File
csv_file_path = "Sample - Superstore.csv"  # Load the Superstore dataset from the current project folder

df = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding='latin-1')

# Print dataset shape, top and bottom rows, descriptive statistics to confirm successful loading
print("\nDataset rows and columns: ", df.shape)
print("=" * 40)

# Print dataset column names
print("\nColumn names:")
print(df.columns.tolist())
print("=" * 40)

print("Top 5 rows :\n", df.head(5))
print("=" * 40)

print("Descriptive Statistics: \n", df.describe())

print("\nDataset loaded successfully! \n")


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


# Goal: Identify if a product is profitable or not and print a message
# for i in range(3):
#     sample_row = df.iloc[i]
#     product = Product(sample_row['Product ID'], sample_row['Category'],
#                       sample_row['Sub-Category'], sample_row['Product Name'],
#                       sample_row['Sales'], sample_row['Quantity'],
#                       sample_row['Discount'], sample_row['Profit'])
#     print(product.show_info())
#     if product.profit_margin() > 20:
#         print("This product is performing well with high profit margin.\n")
#     else:
#         print("Low profit margin. Needs review.\n")


# print("BUSINESS SCENARIO 2: SHIPPING PERFORMANCE")

# # Goal: Check how many orders were shipped in each mode for first few entries
# shipment_counts = {}
# for i in range(5):
#     ship = Shipment(df.iloc[i]['Ship Mode'], df.iloc[i]['Ship Date'], df.iloc[i]['City'])
#     # Count how many times each ship mode appears
#     shipment_counts[ship.ship_mode] = shipment_counts.get(ship.ship_mode, 0) + 1
#     print(ship.show_info())

# print("\nShipping Mode Summary:", shipment_counts)


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

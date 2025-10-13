# Task 1: Object Oriented Programming

# =============================================
# This script demonstrates OOP concepts (Abstraction, Encapsulation, Inheritance, Polymorphism)
# using the Superstore dataset. It models real-world business entities such as
# Customer, Product, Order, Category, and Shipment.


# =================
# ABSTRACTION
# ==================
# Abstraction means hiding complex details and showing only necessary information.
# For example, when creating a Customer object, we don’t need to know how it stores or calculates data.
# We just use its methods like get_customer_info().

# =================
# ENCAPSULATION
# =================
# Encapsulation means keeping data safe by restricting direct access.
# We use private variables (with underscores like _name) and public methods to access them safely.

# ==================
# INHERITANCE
# =================
# Inheritance means one class can reuse or extend another.
# For example, both Category and Product can share common properties like name and ID.

# =================
# POLYMORPHISM
# =================
# Polymorphism means that methods with the same name can behave differently for different classes.
# Example: The show_info() method is defined differently in several classes.


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


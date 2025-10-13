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

#import  required libararies
import pandas as pd
import re

# Load CSV File
csv_file_path = "Sample - Superstore.csv" # Load the Superstore dataset from the current project folder

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
# ================================================================
# Demonstration of all OOP concepts with the dataset
# ================================================================

# Select a sample row from the dataset to create objects
sample_row = df.iloc[1]

# Create Customer object
customer1 = Customer(sample_row["Customer ID"], sample_row["Customer Name"], sample_row["Region"])

# Print results to show function outputs
print("=" * 50)
print("OOP Demonstration using Superstore Dataset")
print("=" * 50)

# Encapsulation & Abstraction Example
print("\nCustomer Info (Encapsulation + Abstraction):")
print(customer1.get_customer_info())

# Count customers using the class method
print("\nNo of Customers: ", customer1.count_customers(df))

# Task 1: Object Oriented Programming
# Load CSV File


import pandas as pd

csv_file_path = "Sample - Superstore.csv"

df = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding='latin-1')

# Print dataset shape, top and bottom rows, descriptive statistics
print("\nDataset rows and columns: ", df.shape)
print("=" * 40)

# Print dataset column names
print("\nColumn names:")
print(df.columns.tolist())
print("=" * 40)

print("Top 10 rows :\n", df.head(10))
print("=" * 40)

print("Bottom 5 rows :\n", df.tail(5))
print("=" * 40)

print("Descriptive Statistics: \n", df.describe())


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


# ================================================================
# Demonstration of all OOP concepts with dataset
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

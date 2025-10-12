#Task 1: Object Oriented Programming
#Load CSV File


import pandas as pd

csv_file_path = "Sample - Superstore.csv"

df = pd.read_csv(csv_file_path, on_bad_lines='skip',encoding= 'latin-1')

#Print dataset shape
print("Dataset rows and columns", df.shape)
print(df.head())
print(df.tail())
print(df.describe())
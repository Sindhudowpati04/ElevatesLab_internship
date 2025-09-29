import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nShape of DataFrame:", df.shape)

if 'Product' in df.columns and 'Sales' in df.columns:
    product_sales = df.groupby('Product')['Sales'].sum()
    print("\nTotal Sales by Product:")
    print(product_sales)

    product_sales.plot(kind='bar', figsize=(8, 5), color='skyblue')
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.show()

if 'Region' in df.columns:
    region_data = df[df['Region'] == 'East']
    print("\nFiltered Data (Region = East):")
    print(region_data.head())
print("\nUsing loc (row labels):")
print(df.loc[0])   

print("\nUsing iloc (row index):")
print(df.iloc[0])  

print("\nMissing values in dataset:")
print(df.isna().sum())

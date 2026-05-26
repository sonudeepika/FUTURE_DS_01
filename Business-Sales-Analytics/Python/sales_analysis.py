import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(
    r'C:\Business-Sales-Analytics\Dataset\superstore.csv',
    encoding='latin1'
)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Info
print("\nDataset Info:")
print(df.info())

# Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", round(total_sales, 2))

# Total Profit
total_profit = df['Profit'].sum()
print("Total Profit:", round(total_profit, 2))

# Total Orders
total_orders = df['Order ID'].nunique()
print("Total Orders:", total_orders)

# Top Categories by Sales
print("\nTop Categories:")
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)

# Profit by Region
print("\nProfit by Region:")
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(region_profit)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Month-Year Column
df['Month'] = df['Order Date'].dt.to_period('M')

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot Monthly Sales Trend
plt.figure(figsize=(12,6))
monthly_sales.plot()

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

plt.savefig('../Dashboard/monthly_sales_trend.png')
plt.show()

# Top 10 Products
print("\nTop 10 Products:")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

# Save Insights to Text File
with open('../Insights.txt', 'w') as file:
    file.write("BUSINESS INSIGHTS\n")
    file.write("====================\n\n")

    file.write(f"Total Sales: {round(total_sales,2)}\n")
    file.write(f"Total Profit: {round(total_profit,2)}\n")
    file.write(f"Total Orders: {total_orders}\n\n")

    file.write("Top Categories by Sales:\n")
    file.write(str(category_sales))
    file.write("\n\n")

    file.write("Profit by Region:\n")
    file.write(str(region_profit))
    file.write("\n\n")

    file.write("Top 10 Products:\n")
    file.write(str(top_products))

print("\nInsights file created successfully!")
import pandas as pd

# Read JSON data
df = pd.read_json("sales.json")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Total per order
df["Total"] = df["Quantity"] * df["Price"]
    # Print full DataFrame
print("\n=== Sales Data ===")
print(df)

# Total sales overall
total_sales = df["Total"].sum()
print(f"\n=== Total Sales Overall ===\n${total_sales:,.2f}")

# Total sales by Product
total_sales_by_Product = df.groupby("Product")["Total"].sum()
print("\n=== Total Sales By Product ===")
print(total_sales_by_Product.to_string())

# Total sales by Region
total_sales_by_Region = df.groupby("Region")["Total"].sum()
print("\n=== Total Sales By Region ===")
print(total_sales_by_Region.to_string())

# Top customers by revenue
top_customers = df.groupby("Customer")["Total"].sum().sort_values(ascending=False)
print("\n=== Top Customers By Revenue ===")
print(top_customers.to_string())

# Daily Sales Trend
daily_sales = df.groupby("Date")["Total"].sum()
print("\n=== Daily Sales Trend ===")
print(daily_sales.to_string())

# Average Order Value
avg_order_value = df["Total"].mean()
print(f"\n=== Average Order Value ===\n${avg_order_value:,.2f}")

# Best-Selling Products (by Quantity)
best_selling = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\n=== Best-Selling Products (by Quantity) ===")
print(best_selling.to_string())

# Orders with Quantity > 2
orders_with_qty_gt2 = df[df["Quantity"] > 2]
print("\n=== Orders With Quantity > 2 ===")
print(orders_with_qty_gt2.to_string(index=False))

# Monthly Sales Trend
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total"].sum()
print("\n=== Monthly Sales Trend ===")
print(monthly_sales.to_string())

# Average Price Per Product
avg_price = df.groupby("Product")["Price"].mean()
print("\n=== Average Price Per Product ===")
print(avg_price.to_string())

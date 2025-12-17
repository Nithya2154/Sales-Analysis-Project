Sales Analysis Project – README
Project Overview

This Python project performs basic sales data analysis using pandas. It reads sales data from a JSON file, calculates totals, aggregates by product, region, and customer, analyzes trends, and identifies key insights like top-selling products and high-quantity orders.

The project is ideal for beginners learning pandas and business data analysis.

Requirements

Python 3.x

pandas library

Install pandas if not already installed:

pip install pandas


A JSON file named sales.json with sales data in the format:

[
  {"OrderID":101,"Date":"2025-01-01","Customer":"Alice","Product":"Laptop","Quantity":1,"Price":1000,"Region":"North"},
  {"OrderID":102,"Date":"2025-01-03","Customer":"Bob","Product":"Mouse","Quantity":5,"Price":25,"Region":"South"}
]

How to Run the Project

Save the code in a file, e.g., sales_analysis.py.

Make sure sales.json is in the same directory.

Run the script:

python sales_analysis.py


The script will print all the analysis results to the console.

Code Explanation
1. Load and Prepare Data
df = pd.read_json("sales.json")
df["Date"] = pd.to_datetime(df["Date"])
df["Total"] = df["Quantity"] * df["Price"]


Reads the sales data from JSON.

Converts Date column to datetime for trend analysis.

Calculates total revenue per order.

2. Total Sales Overall
total_sales = df["Total"].sum()


Sums all order totals to get overall revenue.

3. Total Sales by Product
total_sales_by_Product = df.groupby("Product")["Total"].sum()


Groups sales by product to find which items generated the most revenue.

4. Total Sales by Region
total_sales_by_Region = df.groupby("Region")["Total"].sum()


Groups sales by region to analyze geographical performance.

5. Top Customers by Revenue
top_customers = df.groupby("Customer")["Total"].sum().sort_values(ascending=False)


Finds customers contributing the most revenue.

6. Daily Sales Trend
daily_sales = df.groupby("Date")["Total"].sum()


Aggregates sales by day to observe daily revenue trends.

7. Average Order Value
avg_order_value = df["Total"].mean()


Computes the average revenue per order.

8. Best-Selling Products (by Quantity)
best_selling = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)


Identifies the most sold products by quantity.

9. Orders With Quantity > 2
orders_with_qty_gt2 = df[df["Quantity"] > 2]


Filters and lists orders where customers bought more than 2 units.

10. Monthly Sales Trend
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total"].sum()


Groups sales by month to identify monthly revenue trends.

11. Average Price Per Product
avg_price = df.groupby("Product")["Price"].mean()


Calculates the average selling price for each product.

Sample Output
=== Total Sales Overall ===
$20,000.00

=== Total Sales By Product ===
Laptop      17,000
Mouse       1,075
Keyboard      650

=== Total Sales By Region ===
North      5,000
South      6,000
East       4,000
West       6,725

=== Top Customers By Revenue ===
Bob        6,025
Alice      5,100
Charlie    4,500
...

Project Benefits

Learn pandas basics: read JSON, groupby, sum, mean, filtering.

Analyze sales performance by product, region, and customer.

Track daily and monthly sales trends.

Identify best-selling products and high-value orders.

If you want, I can also update this script to save all results into a structured 
JSON file instead of printing, using headings like your last request. 
This will make it ready for reports or dashboards.

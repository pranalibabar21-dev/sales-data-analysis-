# 📊 Sales Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Dataset
# -------------------------------
try:
    df = pd.read_csv("sales_data (1).csv")
    print("✅ Dataset Loaded Successfully\n")
except:
    print("❌ Error loading dataset. Check file path.")
    exit()

# -------------------------------
# 2. Display Basic Info
# -------------------------------
print("📌 Dataset Preview:")
print(df.head())

print("\n📌 Columns:")
print(df.columns)

# -------------------------------
# 3. Data Cleaning
# -------------------------------
# Remove missing values
df.dropna(inplace=True)

# Create Total_Sales column if not present
if 'Total_Sales' not in df.columns:
    df['Total_Sales'] = df['Quantity'] * df['Price']

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# -------------------------------
# 4. Data Analysis
# -------------------------------

# Top 5 Products
top_products = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(5)

# Sales Trend (Monthly)
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

# Region-wise Sales
region_sales = df.groupby('Region')['Total_Sales'].sum()

# -------------------------------
# 5. Visualization
# -------------------------------
sns.set(style="whitegrid")

# -------------------------------
# 5. Visualization (FIXED)
# -------------------------------
sns.set(style="whitegrid")

# 📊 Bar Chart
plt.figure(figsize=(8,5))
top_products.plot(kind='bar', color='skyblue')
plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# IMPORTANT: Clear previous plot
plt.clf()

# 📈 Line Chart
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.clf()

# 🥧 Pie Chart
plt.figure(figsize=(6,6))
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Region-wise Sales Distribution")
plt.ylabel('')
plt.tight_layout()
plt.show()

# -------------------------------
# 6. Insights
# -------------------------------
print("\n📊 Key Insights:")

print(f"✔ Top Selling Product: {top_products.idxmax()}")
print(f"✔ Highest Sales Region: {region_sales.idxmax()}")
print(f"✔ Total Revenue: {df['Total_Sales'].sum():.2f}")
plt.show(block=True)
import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "clean_products.csv"
)

df = pd.read_csv(file_path)

# Top 10 expensive laptops
top10 = df.nlargest(10, "Price")

plt.figure(figsize=(12, 6))
plt.barh(top10["Title"], top10["Price"])
plt.xlabel("Price")
plt.title("Top 10 Most Expensive Laptops")
plt.tight_layout()

plt.show()
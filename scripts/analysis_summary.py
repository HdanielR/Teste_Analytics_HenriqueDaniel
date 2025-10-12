# analysis_summary.py
# This script summarizes total sales per product from data_clean.csv
import pandas as pd
df = pd.read_csv("data_clean.csv")
sales_by_product = df.groupby(["Produto","Categoria"], as_index=False).agg({"Quantidade":"sum","TotalVenda":"sum"})
sales_by_product = sales_by_product.sort_values("TotalVenda", ascending=False)
print(sales_by_product.head(10))
print("\nTop product:", sales_by_product.iloc[0]["Produto"], "with total sales", sales_by_product.iloc[0]["TotalVenda"])

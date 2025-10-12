# visualization.py
# Generates a monthly trend line plot from data_clean.csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_clean.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M").astype(str)
monthly = df.groupby("Mes", as_index=False).agg({"TotalVenda":"sum"})
monthly = monthly.sort_values("Mes")
plt.figure(figsize=(10,5))
plt.plot(monthly["Mes"], monthly["TotalVenda"], marker='o')
plt.xticks(rotation=45)
plt.title("Tendência Mensal de Vendas (Total em Reais)")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas (R$)")
plt.tight_layout()
plt.savefig("monthly_trend.png")

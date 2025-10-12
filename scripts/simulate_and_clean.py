# simulate_and_clean.py
"""
Gera dados simulados de vendas (2023) e efetua limpeza básica, salvando data_clean.csv.
Este script foi usado para criar os datasets entregues no repositório.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def parse_date(x):
    for fmt in ("%Y-%m-%d","%Y/%m/%d","%d-%m-%Y","%d/%m/%Y"):
        try:
            return datetime.strptime(x, fmt).date()
        except:
            continue
    return pd.NaT

def to_int(x):
    try:
        return int(float(str(x).replace(",",".")))
    except:
        return np.nan

def to_float(x):
    if pd.isna(x):
        return np.nan
    try:
        return float(str(x).replace(",","."))
    except:
        return np.nan

def main():
    products = [
        ("Cacau Premium", "Alimentos"),
        ("Cacau Tradicional", "Alimentos"),
        ("Adubo A", "Insumos"),
        ("Adubo B", "Insumos"),
        ("Pesticida X", "Insumos"),
        ("Ferramenta Y", "Ferramentas"),
        ("Semente Z", "Insumos"),
        ("Embalagem 1kg", "Embalagens"),
        ("Embalagem 500g", "Embalagens"),
        ("Fertilizante Liquido", "Insumos")
    ]
    n = 180
    start = datetime(2023,1,1)
    end = datetime(2023,12,31)
    days = (end - start).days + 1
    dates = [start + timedelta(days=int(x)) for x in np.random.randint(0, days, size=n)]

    rows = []
    for i in range(n):
        prod, cat = random.choice(products)
        qty = int(np.random.choice([1,1,2,3,5,10,20], p=[0.25,0.2,0.2,0.15,0.1,0.05,0.05]))
        price = round(abs(np.random.normal(loc=50 if "Cacau" in prod else 30, scale=20)),2)
        if np.random.rand() < 0.03:
            price = None
        if np.random.rand() < 0.02:
            qty = None
        id_val = f"ID{1000 + i}"
        rows.append([id_val, dates[i].strftime("%Y-%m-%d"), prod, cat, qty, price])

    # add some duplicates and bad formats
    rows.append(rows[10])
    rows.append([rows[20][0], rows[20][1], rows[20][2], rows[20][3], rows[20][4], rows[20][5]])
    rows.append([ "ID9999", "2023/05/15", "Cacau Premium", "Alimentos", "3", "45,50" ])
    rows.append([ "ID10000", "15-06-2023", "Adubo A", "Insumos", "two", 25.0 ])

    df = pd.DataFrame(rows, columns=["ID","Data","Produto","Categoria","Quantidade","Preço"])
    df.to_csv("data_simulated_raw.csv", index=False)
    print("Simulated raw saved: data_simulated_raw.csv")

    # Cleaning
    df_clean = df.copy()
    df_clean["Data"] = df_clean["Data"].apply(lambda x: parse_date(x) if pd.notna(x) else pd.NaT)
    df_clean["Quantidade"] = df_clean["Quantidade"].apply(to_int)
    df_clean["Preço"] = df_clean["Preço"].apply(to_float)
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.sort_values(by=["ID","Data"], ascending=[True,False])
    df_clean = df_clean.drop_duplicates(subset=["ID"], keep="first")
    df_clean["Quantidade"] = df_clean["Quantidade"].fillna(1).astype(int)
    med_by_prod = df_clean.groupby("Produto")["Preço"].median()
    def fill_price(row):
        if pd.notna(row["Preço"]):
            return row["Preço"]
        prod = row["Produto"]
        if pd.notna(med_by_prod.get(prod)):
            return med_by_prod.get(prod)
        return df_clean["Preço"].median()
    df_clean["Preço"] = df_clean.apply(fill_price, axis=1)
    df_clean["Preço"] = df_clean["Preço"].astype(float)
    df_clean["Data"] = df_clean["Data"].fillna(pd.to_datetime("2023-01-01").date())
    df_clean["TotalVenda"] = df_clean["Quantidade"] * df_clean["Preço"]
    df_clean.to_csv("data_clean.csv", index=False)
    print("Clean dataset saved: data_clean.csv")

if __name__ == "__main__":
    main()

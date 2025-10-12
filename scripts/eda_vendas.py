# eda_vendas.py
"""
Análise Exploratória de Dados de Vendas
Gera gráficos de tendência mensal, top 10 produtos e Pareto.
Autor: Henrique Daniel
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Carregar o dataset limpo
    df = pd.read_csv("data_clean.csv", parse_dates=["Data"])

    # Garantir colunas numéricas
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(1).astype(int)
    df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce").fillna(df["Preço"].median())
    df["Total_Venda"] = df["Quantidade"] * df["Preço"]

    # === 1. Gráfico de tendência mensal ===
    vendas_mensais = (
        df.groupby(df["Data"].dt.to_period("M"))["Total_Venda"]
        .sum()
        .reset_index()
    )
    vendas_mensais["Data"] = vendas_mensais["Data"].dt.to_timestamp()

    plt.figure(figsize=(10, 5))
    plt.plot(vendas_mensais["Data"], vendas_mensais["Total_Venda"], marker="o")
    plt.title("Tendência de Vendas Mensais - 2023")
    plt.xlabel("Mês")
    plt.ylabel("Total de Vendas (R$)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_vendas_mensais.png", dpi=300)
    print("Salvo: grafico_vendas_mensais.png")
    plt.close()

    # === 2. Top 10 produtos mais vendidos ===
    top_produtos = (
        df.groupby("Produto")["Total_Venda"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    plt.figure(figsize=(10, 6))
    top_produtos.plot(kind="barh")
    plt.title("Top 10 Produtos - Receita")
    plt.xlabel("Total de Vendas (R$)")
    plt.tight_layout()
    plt.savefig("top10_produtos.png", dpi=300)
    print("Salvo: top10_produtos.png")
    plt.close()

    # === 3. Gráfico de Pareto ===
    sales_sorted = df.groupby("Produto")["Total_Venda"].sum().sort_values(ascending=False)
    acumulado = sales_sorted.cumsum() / sales_sorted.sum() * 100

    fig, ax1 = plt.subplots(figsize=(10,6))
    ax1.bar(sales_sorted.index, sales_sorted.values)
    ax1.set_xticklabels(sales_sorted.index, rotation=45, ha='right')
    ax1.set_ylabel("Vendas (R$)")

    ax2 = ax1.twinx()
    ax2.plot(sales_sorted.index, acumulado, color="red", marker="D")
    ax2.set_ylabel("% Acumulado")
    plt.title("Pareto - Receita por Produto")
    plt.tight_layout()
    plt.savefig("pareto_vendas.png", dpi=300)
    print("Salvo: pareto_vendas.png")
    plt.close()

if __name__ == "__main__":
    main()

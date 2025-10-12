-- consultas_sql.sql
-- Assunção: tabela sales_clean corresponde ao arquivo data_clean.csv que contém colunas:
-- ID, Data, Produto, Categoria, Quantidade, Preço, TotalVenda

-- 1) Listar produto, categoria e soma total de vendas por produto, ordenado desc
SELECT Produto, Categoria, SUM(Quantidade * Preço) AS TotalVendas
FROM sales_clean
GROUP BY Produto, Categoria
ORDER BY TotalVendas DESC;

-- 2) Identificar produtos que venderam menos no mês de junho de 2024
-- Assunção: criamos uma tabela sales_june_2024 (arquivo sales_june_2024.csv) com registros de junho/2024.
-- A consulta abaixo mostra produtos com Quantidade total baixa (ex: <= 1) em junho/2024.
SELECT Produto, Categoria, SUM(Quantidade) AS Quantidade_Junho_2024, SUM(Quantidade * Preço) AS TotalVendas_Junho_2024
FROM sales_june_2024
WHERE strftime('%Y-%m', Data) = '2024-06' OR Data LIKE '2024-06-%'
GROUP BY Produto, Categoria
HAVING Quantidade_Junho_2024 <= 1
ORDER BY Quantidade_Junho_2024 ASC, TotalVendas_Junho_2024 ASC;

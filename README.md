# 🧠 Teste_Analytics_HenriqueDaniel - Henrique Daniel Resende

Repositório criado para o **Teste Técnico para Estagiário de Analytics - Quod**.  
O objetivo é demonstrar habilidades em **Python**, **análise de dados**, **visualização** e **interpretação de resultados**.

---

## 📁 Estrutura do Repositório

```
Teste_Analytics_HenriqueDaniel/
│
├── data/
│   ├── data_raw.csv               # Dados simulados brutos
│   ├── data_clean.csv             # Dados após limpeza
│   ├── sales_june_2024.csv        # vendas de junho 2024
│
├── scripts/
│   ├── 01_gerar_e_limpar_dados - simulate_and_clean.py # Simulação e tratamento do dataset de vendas
│   ├── 02_analise_exploratoria - eda_vendas.py # Análises e visualizações de vendas
│   ├── visualization.py # Gera gráfico de tendência mensal
│   ├── analysis_summary.py # Calcula totais de vendas por produto
│   ├── clean_data.py # Executa a limpeza chamando a função principal
│
├── sql/
│   └── consultas_sql.sql          # Consultas SQL solicitadas no desafio
│
├── relatorio_insights.md          # Relatório textual com principais resultados e insights
├── README.md                      # Este arquivo
└── requirements.txt               # Dependências do projeto
```

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/Teste_Analytics_HenriqueDaniel.git
cd Teste_Analytics_HenriqueDaniel
```

### 2. Criar e ativar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar os scripts
1. **Gerar e limpar dados:**
   ```bash
   python scripts/simulate_and_clean.py
   ```
   → Gera o dataset simulado e o arquivo `data_clean.csv`.

2. **Realizar análise exploratória:**
   ```bash
   python scripts/eda_vendas.py
   ```
   → Cria gráficos e salva visualizações na pasta `/output` (se aplicável).

---

## 🧩 Parte 1 – Programação em Python

### 🧾 Simulação de Dados
Foi gerado um dataset com 50 registros representando vendas de produtos ao longo de **2023**, com as colunas:
- **ID**: identificador único da venda  
- **Data**: data entre 01/01/2023 e 31/12/2023  
- **Produto**: nome do produto  
- **Categoria**: categoria do produto  
- **Quantidade**: unidades vendidas  
- **Preço**: valor unitário  

### 🧹 Limpeza de Dados
Foram aplicadas as seguintes etapas:
- Tratamento de valores ausentes (remoção/substituição com média)
- Remoção de duplicatas
- Conversão de colunas de data e numéricas para tipos adequados
- Exportação final para `data_clean.csv`

### 📊 Análises Realizadas
- Cálculo do total de vendas (`Quantidade * Preço`) por produto.  
- Identificação do produto com **maior volume total de vendas**.  
- Geração de um **gráfico de linha mensal** mostrando a tendência de vendas ao longo de 2023.  
- Identificação de **padrões e insights** observados.

---

## 🧮 Parte 2 – SQL

As consultas SQL foram elaboradas considerando a mesma estrutura do dataset tratado.  
Arquivo: `sql/consultas_sql.sql`

1. **Total de vendas por produto e categoria (ordenado decrescente):**
   ```sql
   SELECT Produto, Categoria, SUM(Quantidade * Preco) AS Total_Vendas
   FROM vendas
   GROUP BY Produto, Categoria
   ORDER BY Total_Vendas DESC;
   ```

2. **Produtos com menor volume de vendas no mês de junho/2024:**
   ```sql
   SELECT Produto, SUM(Quantidade * Preco) AS Total_Junho
   FROM vendas
   WHERE strftime('%Y-%m', Data) = '2024-06'
   GROUP BY Produto
   ORDER BY Total_Junho ASC;
   ```

---

## 🧠 Parte 3 – Interpretação de Resultados

Arquivo: `relatorio_insights.md`

O relatório apresenta:
- Principais **tendências de vendas** mensais;
- Identificação de **picos e quedas sazonais**;
- Sugestões de **ações comerciais** baseadas nas análises.

---

## 🧩 Suposições Adotadas

- Os dados foram **simulados** aleatoriamente, com base em categorias e produtos genéricos.  
- Considerou-se um cenário de vendas **uniforme ao longo de 2023**, sem influências externas.  
- Todos os valores monetários estão em **Reais (R$)**.  
- Os produtos e categorias são ilustrativos e não correspondem a dados reais.

---

## 📈 Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas** – manipulação e análise de dados  
- **NumPy** – operações numéricas  
- **Matplotlib / Seaborn** – visualização de dados  
- **SQLite (simulado)** – consultas SQL  
- **Jupyter / VSCode** – ambiente de desenvolvimento  

---

## 💡 Possíveis Melhorias Futuras

- Expandir o volume de dados para testes estatísticos mais robustos.  
- Incluir variáveis externas (como sazonalidade ou campanhas promocionais).  
- Criar dashboards interativos com **Plotly** ou **Streamlit**.  

---

## ✉️ Contato

**Henrique Daniel Resende**  
E-mail: danielgoryz008@gmail.com (utilizado no processo seletivo)
LinkedIn: https://www.linkedin.com/in/hdresende

---

🧩 *Desenvolvido como parte do processo seletivo de Estágio em Analytics - Quod.*

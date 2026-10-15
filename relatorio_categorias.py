import pandas as pd

vendas = pd.read_csv('vendas_pandas.csv', encoding='utf-8')
vendas.columns = vendas.columns.str.strip().str.lower()
vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]
print(vendas.groupby("cidade")["total"].sum())



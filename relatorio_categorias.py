import pandas as pd

vendas = pd.read_csv('vendas_pandas.csv', encoding='utf-8')
vendas.columns = vendas.columns.str.strip().str.lower()
vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]

resumo = vendas.groupby("categoria").agg(
    total_vendido=("total", "sum"),
    itens_vendidos=("quantidade", "sum"),
    preco_medio=("preco_unitario", "mean")
).reset_index()
resumo = resumo.sort_values(by="total_vendido", ascending=False)
print(resumo)

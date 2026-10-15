import pandas as pd

sujo = pd.read_csv("sujo.csv")
print(sujo.shape)
print(sujo.isna().sum())
import pandas as pd
from script import Sheet
from script import Sheet
import os

class Calculos:
    def __init__(self, tabela):
        self.tabela = tabela

    def media(self):
        total = self.tabela["Total"]
        media = total.sum() / total.count()
        
        return media
    
    def mediana(self):
        orderTotal = self.tabela.sort_values(by="Total")
        mediana = orderTotal["Total"].median()
        return mediana

    def desvioPadrao(self):
        dpTotal = self.tabela["Total"].std()
        return dpTotal
    
    def quartis(self):
        values_total = self.tabela.sort_values(by="Total")
        quartis = values_total.describe(percentiles=[.25, .5, .75]).loc[['25%', '50%', '75%']]
        q1 = quartis.loc['25%'].iloc[0]
        q2 = quartis.loc['50%'].iloc[0]
        q3 = quartis.loc['75%'].iloc[0]
        quartis_string = f"Q1 = {q1}, Q2 = {q2}, Q3 = {q3}"
        return quartis_string

if __name__ == "__main__":
    
    values = {
        "path" : f"{os.getcwd()}/import/",
        "file" : "tabelaPooFormatadaIndice.xlsx"
    }

    table = Sheet(values)
    table = Sheet(values)
    df = table.read()
    
    calculos =  Calculos(df)
    print(f"Média: {calculos.media()}")
    print(f"Mediana: {calculos.mediana()}")
    print(f"Desvio Padrao: {calculos.desvioPadrao()}")
    print(f"Quartis: {calculos.quartis()}")

# 200.094395635249
# count    194.000000
# mean     177.048416
# std       54.928471
# min       61.589493
# 25%      139.967985
# 50%      200.094396
# 75%      212.908177
# max      253.487580
# Name: Total, dtype: float64
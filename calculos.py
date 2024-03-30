import pandas as pd
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

if __name__ == "__main__":
    
    values = {
        "path" : f"{os.getcwd()}\\py-sci\\import\\",
        "file" : "tabelaPooFormatadaIndice.xlsx"
    }

    table = Sheet(values)
    df = table.read()
    
    calculos =  Calculos(df)
    print(f"Média: {calculos.media()}")
    print(f"Mediana: {calculos.mediana()}")
    print(f"Desvio Padrao: {calculos.desvioPadrao()}")

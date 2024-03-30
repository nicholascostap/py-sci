import pandas as pd
from script import Sheet
import os

class AnaliseInicial:
    def __init__(self, tabela):
        self.dataFrame = tabela
    

    def qtdElementos(self):
        quantidade = self.dataFrame["Total"].count()
        return quantidade
    
    def tipoColunas(self):
        df["Data"] = pd.to_datetime(self.dataFrame["Data"])
        colunas = self.dataFrame.dtypes
        return colunas

    


if __name__ == "__main__":
    
    values = {
        "path" : f"{os.getcwd()}\\py-sci\\import\\",
        "file" : "tabelaPooFormatadaIndice.xlsx"
    }

    table = Sheet(values)
    df = table.read()
    
    calculos =  AnaliseInicial(df)
    print(f'Qtd Elementos: {calculos.qtdElementos()}')
    print(f'Colunas e Tipos: {calculos.tipoColunas()}')
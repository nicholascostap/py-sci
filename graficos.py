import pandas as pd
import os
from script import Sheet
import numpy as np
import matplotlib.pyplot as plt

class Graficos:
    def __init__(self, tabela):
        self.dataFrame = tabela

    def graficoExemplo(self):
        x = self.dataFrame["Data"]
        y = self.dataFrame["Total"]

        plt.figure, ax = plt.subplots() 
        ax.plot(x, y)
    def indiceTempo(self):
        x = self.dataFrame["Data"]
        y = self.dataFrame["Total"]

        plt.plot(x, y)
        plt.xticks(rotation=35, ha='right')
        intervalo = 6
        plt.xticks(range(0, len(x), intervalo))
        plt.xlabel('x = Data')
        plt.ylabel('y = Total')
        plt.title("Índice vs Tempo")
        plt.tight_layout()
        grafico = plt.show()
        return grafico
    
    def getBoxplot(self):
        x = self.dataFrame['Total']
        plt.boxplot(x,showfliers=True,flierprops=dict(marker='o',markersize=8,markerfacecolor='red'))
        grafico = plt.show()
        return grafico
    

if __name__ == "__main__":
    
    values = {
        "path" : f"{os.getcwd()}\\py-sci\\import\\",
        "file" : "tabelaPooFormatadaIndice.xlsx"
    }

    table = Sheet(values)
    df = table.read()

    grafico = Graficos(df)
    grafico.graficoExemplo()
    grafico.indiceTempo()
    grafico.getBoxplot()

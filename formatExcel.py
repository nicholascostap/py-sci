# Manipulação de Tabela
# Organizando dados para utilização do projeto

import pandas as pd
import os

class FormatExcel:
    def __init__(self, caminho) :
        self.caminho = caminho
    
    def formatarExcel(self):
        # Lendo arquivo excel
        tabela = pd.read_excel(f"{os.getcwd()}\\{self.caminho}")

        # convertendo para data a coluna Data
        datas = pd.to_datetime(tabela["Data"])

        # atribuindo a coluna Data, as novas datas formatadas
        tabela["Data"] = datas.dt.strftime('%Y-%m-01')

        # verificando duplicidades de datas
        duplicados = tabela["Data"].duplicated()
        ha_duplicados = duplicados.any()
        if ha_duplicados:
            tabela = tabela.drop_duplicates(subset=["Data"], keep="first")
            
        # salvando em um arquivo excel a nova planilha
        tabela.to_excel(f"{os.getcwd()}\\import\\tabelaPooFormatadaIndice.xlsx",index=False)
        # print(tabela["Total"])


caminho = f"import\\projetoPOO.xlsx"
print(os.getcwd()+'\\'+caminho)
formatarTabela = FormatExcel(caminho)
formatarTabela.formatarExcel()
import pandas as pd
import os
from datetime import datetime
from planilha import Planilha

class Calculo:
    """Classe para cálculos estatísticos."""
    def __init__(self, tabela: pd.DataFrame):
        self.tabela: pd.DataFrame = tabela
        self._media: float = 0
        self._mediana: float = 0
        self._desvio_padrao: float = 0
        self._coeficiente_variacao: float = 0
        self._quartis: dict = {
                                'q1': 0, 
                                'q2': 0, 
                                'q3': 0
                            }

    def media(self, coluna) -> float:
        """Calcula a média dos valores da coluna informada.\n
        Args:
            `coluna` (str): Nome da coluna a ser calculada.
        Returns:
            `media` (float): Média dos valores da coluna."""
        
        total : pd.Series = self.tabela[coluna]
        media = total.sum() / total.count()
        return media

    def mediana(self, coluna : str) -> float:
        """Calcula a mediana dos valores da coluna.\n
        Args:
            `coluna` (str): Nome da coluna a ser calculada.
        Returns:
            `mediana` (float): Mediana dos valores da coluna."""
        
        valores_ordenados = self.tabela.sort_values(by=coluna)
        mediana = valores_ordenados[coluna].median()
        return mediana


    def desvio_padrao(self, coluna: str) -> float:
        """Calcula o desvio padrão dos valores da coluna.\n
        Args:
            `coluna` (str): Nome da coluna a ser calculada.
        Returns:
            `desvio_padrao` (float): Desvio padrão dos valores da coluna."""
        
        desvio_padrao = self.tabela[coluna].std()
        return desvio_padrao

    def coeficiente_variacao(self, coluna: str) -> float:
        """Calcula o coeficiente de variação dos valores da coluna.\n
        Args:
            `coluna` (str): Nome da coluna a ser calculada.
        Returns:
            `coeficiente_variacao` (float): Coeficiente de variação dos valores da coluna."""
        
        coeficiente_variacao = self.tabela[coluna].std() / self.tabela[coluna].mean()
        return coeficiente_variacao
    
    def quartis(self, coluna: str) -> tuple:
        """Calcula os quartis dos valores da coluna.
        Args:
            `coluna` (str): Nome da coluna a ser calculada.
        Returns:
            `quartis` (dict): Dicionário com os valores dos quartis."""
        valores_ordenados = self.tabela.sort_values(by=coluna)
        quartis = valores_ordenados.describe(percentiles=[.25, .5, .75]).loc[['25%', '50%', '75%']]
        return {
            'q1' : quartis.loc['25%'].iloc[0],
            'q2' : quartis.loc['50%'].iloc[0],
            'q3' : quartis.loc['75%'].iloc[0]
        }

if __name__ == "__main__":

    data_atual = datetime.now().strftime("%Y-%m-%d")
    
    caminho = os.getcwd()
    caminho += f"//export//{data_atual}//"
        
    parametos = {
        "caminho_origem" : f"{caminho}",
        "arquivo" : "fipezap-serieshistoricas-formatado",
        "colunas" : ["Data", "Total"]
    }

    tabela = Planilha(parametos)
    df = tabela.ler()
    
    calculos = Calculo(df)
    
    calculos._media = calculos.media(coluna='Total')
    calculos._mediana = calculos.mediana(coluna='Total')
    calculos._desvio_padrao = calculos.desvio_padrao(coluna='Total')
    calculos._coeficiente_variacao = calculos.coeficiente_variacao(coluna='Total')
    calculos._quartis = calculos.quartis(coluna='Total')

    print(f"Média: {calculos._media}")
    print(f"Mediana: {calculos._mediana}")
    print(f"Desvio padrão: {calculos._desvio_padrao}")
    print(f"Coeficiente de variação: {calculos._coeficiente_variacao}")
    print(f"Quartis: {[f'Q{i+1}: {value}' for i, value in enumerate(calculos._quartis.values())]}")
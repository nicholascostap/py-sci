import pandas as pd
import os
from datetime import datetime
from planilha import Planilha

class Calculo:
    """Classe contendo os cálculos e resultados estatísticos
    da tabela FipeZap processada na planilha.\n
    Args:
        `tabela` (pd.DataFrame): Tabela com os dados a serem calculados.
    Attributes:
        `_media` (float): Média dos valores da coluna.
        `_mediana` (float): Mediana dos valores da coluna.
        `_desvio_padrao` (float): Desvio padrão dos valores da coluna.
        `_coeficiente_variacao` (float): Coeficiente de variação dos valores da coluna.
        `_quartis` (dict): Dicionário com os valores dos quartis.
    """
    
    def __init__(self, tabela: pd.DataFrame):
        self.tabela: pd.DataFrame = tabela
        self._media: float = 0.0
        self._mediana: float = 0.0
        self._desvio_padrao: float = 0.0
        self._coeficiente_variacao: float = 0.0
        self._quartis: dict[float] = {
                                'q1': 0.0, 
                                'q2': 0.0, 
                                'q3': 0.0
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
            `coeficiente_variacao` (float): Coeficiente de variação 
            dos valores da coluna."""
        
        coeficiente_variacao = self.tabela[coluna].std() / self.tabela[coluna].mean()
        return coeficiente_variacao
    
    def quartis(self, coluna: str) -> dict:
        """Calcula os quartis dos valores da coluna.
        Args:
            `coluna` (str): Nome da coluna a ser calculada.
        Returns:
            `quartis` (dict): Dicionário com os valores dos quartis."""
        
        valores_ordenados = self.tabela.sort_values(by=coluna)
        quartis = valores_ordenados.describe(
                        percentiles=[.25, .5, .75]).loc[['25%', '50%', '75%']]
        return {
            'q1' : quartis.loc['25%'].iloc[0],
            'q2' : quartis.loc['50%'].iloc[0],
            'q3' : quartis.loc['75%'].iloc[0]
        }
    
    def exibir(self) -> None:
        """Exibe os resultados dos cálculos."""
        
        print(f"Média: {self._media}")
        print(f"Mediana: {self._mediana}")
        print(f"Desvio padrão: {self._desvio_padrao}")
        print(f"Coeficiente de variação: {self._coeficiente_variacao}")
        print(f"Quartis: {[f'Q{i+1}: {value}' for i, value in enumerate(self._quartis.values())]}")
    
    def main(self):
        """Executa os cálculos e exibe os resultados."""
        
        self._media = self.media(coluna='Total')
        self._mediana = self.mediana(coluna='Total')
        self._desvio_padrao = self.desvio_padrao(coluna='Total')
        self._coeficiente_variacao = self.coeficiente_variacao(coluna='Total')
        self._quartis = self.quartis(coluna='Total')
        self.exibir()

        print("Calculos realizados com sucesso!")

if __name__ == "__main__":

    data_atual = datetime.now().strftime("%Y-%m-%d")
    
    caminho = os.getcwd()
    caminho += f"//export//{data_atual}//"
        
    parametos = {
        "caminho_origem" : f"{caminho}",
        "arquivo" : "fipezap-serieshistoricas-formatado",
        "colunas" : ["Data", "Total"]
    }

    planilha = Planilha(parametos)
    tabela = planilha.ler()
    
    calculos = Calculo(tabela)
    calculos.main()
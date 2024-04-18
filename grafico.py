import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from planilha import Planilha
from datetime import datetime

class Grafico:
    """Classe contendo os gráficos a serem gerados\n
    à partir da tabela FipeZap processada na planilha.\n
    Attributes:
        `tabela` (pd.DataFrame): Tabela com os dados a serem plotados.
        `eixo_x` (pd.Series): Eixo X do gráfico.
        `eixo_y` (pd.Series): Eixo Y do gráfico.
        `indice_tempo` (plt): Gráfico de Índices em relação à Tempo.
        `boxplot` (plt): Gráfico de Boxplot.
        `distribuicao_normal` (plt): Gráfico de Distribuição Normal.
    """

    def __init__(self, tabela : pd.DataFrame):
        self.tabela: pd.DataFrame = tabela
        self.eixo_x: pd.Series = pd.Series()
        self.eixo_y: pd.Series = pd.Series()
        self.indice_tempo: plt = plt
        self.boxplot: plt = plt
        self.distribuicao_normal: plt = plt
        self.regressao_linear: plt = plt

    def definir_legendas(self, 
        grafico: plt,
        titulo: str,
        eixo_x: pd.Series=None,
        eixo_y: pd.Series=None) -> None:
        """Define as legendas dos eixos X, Y e título do gráfico.\n
        Args:
            `grafico` (plt): Gráfico à definir as legendas.
            `titulo` (str): Título do gráfico.
            `eixo_x` (pd.Series): Eixo X do gráfico. *Opcional
            `eixo_y` (pd.Series): Eixo Y do gráfico. *Opcional"""
        
        tem_eixo_x: bool = eixo_x is not None
        tem_eixo_y: bool = eixo_y is not None

        if tem_eixo_x:
            grafico.xlabel(f'X = {self.eixo_x.name}')
        if tem_eixo_y:
            grafico.ylabel(f'Y = {self.eixo_y.name}')
        
        grafico.title(titulo)

    def definir_localizacao_eixo(self, 
        grafico: plt, 
        eixo: str,
        rotacao: int, 
        intervalo: int) -> None:
        """Define a localização dos eixos do gráfico.\n
        Args:
            `grafico` (plt): Gráfico à definir a localização dos eixos.
            `eixo` (str): Nome do eixo a ser definido.
            `rotacao` (int): Ângulo de rotação do eixo X.
            `intervalo` (int): Intervalo entre os valores do eixo X.
        """
        
        match eixo:

            case 'eixo_x':
                grafico.xticks(rotation=rotacao, ha='right')
                grafico.xticks(range(0, len(self.eixo_x), intervalo))

            case 'eixo_y':
                grafico.yticks(rotation=rotacao, ha='right')
                grafico.yticks(range(0, len(self.eixo_y), intervalo))

    def gerar_indice_tempo(self, intervalo : int) -> plt:
        """Gera o gráfico de Índices em relação à Tempo
        com os dados plotados e retorna o gráfico gerado.\n
        Args:
            `intervalo` (int): Intervalo entre os valores do eixo X.
        """

        indice_tempo : plt = plt

        eixo_x: pd.Series = self.eixo_x
        eixo_y: pd.Series = self.eixo_y
        
        indice_tempo.plot(eixo_x, eixo_y)

        self.definir_localizacao_eixo(indice_tempo, eixo='eixo_x', 
                        rotacao=35, intervalo=intervalo)
        
        titulo : str = 'Índice X Tempo'
        
        self.definir_legendas(indice_tempo, 
                            titulo, eixo_x, eixo_y)

        indice_tempo.tight_layout()
        return indice_tempo
    
    def gerar_boxplot(self) -> plt:
        """Gera o gráfico de Boxplot com os dados plotados 
        e retorna o gráfico gerado."""

        boxplot: plt = plt

        eixo_x: pd.Series = self.eixo_x

        boxplot.boxplot(eixo_x, showfliers=True,
            flierprops={
                'marker': 'o', 
                'markersize': 8, 
                'markerfacecolor': 'red'
            }
        )
        
        titulo = 'Boxplot'
        self.definir_legendas(boxplot, titulo, eixo_x)
        return boxplot

    def gerar_distribuicao_normal(self) -> plt:
        """Gera o gráfico de Distribuição Normal
        com os dados plotados e retorna o gráfico gerado."""

        distribuicao_normal: plt = plt
        eixo_x: pd.Series = self.eixo_x

        distribuicao_normal.hist(eixo_x, 
            bins=10, edgecolor='black', color='skyblue')
        
        titulo = 'Distribuição Normal'
        
        self.definir_legendas(distribuicao_normal, 
                            titulo, eixo_x)
        
        return distribuicao_normal
    
    def gerar_regressao_linear(self) -> plt:
        """Gera o gráfico de Regressão Linear
        com os dados plotados e retorna o gráfico gerado."""

        regressao_linear: plt = plt
        eixo_x: pd.Series = self.eixo_x
        eixo_y: pd.Series = self.eixo_y

        eixo_x = self.converter_datas(eixo_x)
        eixo_y = self.converter_numeros(eixo_y)

        coeficiente = np.polyfit(eixo_x, eixo_y, 1)
        polinomio = np.poly1d(coeficiente)

        regressao_linear.plot(eixo_x, polinomio(eixo_x), color='red')
        regressao_linear.scatter(eixo_x, eixo_y)

        titulo = 'Regressão Linear'
        
        self.definir_legendas(regressao_linear, 
                            titulo, eixo_x, eixo_y)
        
        return regressao_linear
    
    def converter_datas(self, eixo: pd.Series) -> pd.Series:
        """Converte os dados do eixo para o formato 'datetime'.\n
        Args:
            `eixo` (pd.Series): Eixo à ser convertido.
        Returns:
            `pd.Series`: Eixo convertido para o formato 'datetime'."""

        eixo = pd.to_datetime(eixo, format='%Y-%m-%d', errors='coerce')
        eixo = eixo.dropna()
        return eixo
    
    def converter_numeros(self, eixo: pd.Series):
        """Converte os dados do eixo para o formato 'numeric'.\n
        Args:
            `eixo` (pd.Series): Eixo à ser convertido.
        Returns:
            `pd.Series`: Eixo convertido para o formato 'numeric'."""

        eixo = pd.to_numeric(eixo, errors='coerce')
        eixo = eixo.dropna()
        return eixo

    def exibir(self, grafico: plt) -> None:
        """Exibe o gráfico gerado.
        Args:
            `grafico` (plt): Gráfico à ser exibido."""
        
        grafico.show()

    def salvar(self, grafico: plt, nome: str) -> None:
        """Salva os gráficos gerados.
        Args:
            `grafico` (plt): Gráfico à ser salvo.
            `nome` (str): Nome do arquivo a ser salvo."""
        
        data_atual = datetime.now().strftime("%Y-%m-%d")
        
        caminho = os.getcwd()
        caminho += f"//export//{data_atual}//graficos//"
        
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        
        grafico.savefig(f"{caminho}//grafico-{nome}.png")

    def exportar(self, grafico: plt, nome: str) -> str:
        """Salva, exibe e fecha o gráfico gerado."""
        self.salvar(grafico, nome)
        self.exibir(grafico)
        grafico.close()

    def main(self) -> None:
        """Método principal para gerar e exportar os gráficos."""
        
        self.eixo_x = self.tabela['Data']
        self.eixo_y = self.tabela['Total']

        self.indice_tempo = self.gerar_indice_tempo(intervalo=12)
        self.exportar(self.indice_tempo, 'indice-tempo')

        self.eixo_x = self.tabela['Total']
        self.eixo_y = None

        self.boxplot = self.gerar_boxplot()
        self.exportar(self.boxplot, 'boxplot')

        self.distribuicao_normal = self.gerar_distribuicao_normal()
        self.exportar(self.distribuicao_normal, 'distribuicao-normal')

        self.eixo_x = self.tabela['Data']
        self.eixo_y = self.tabela['Total']

        self.regressao_linear = self.gerar_regressao_linear()
        self.exportar(self.regressao_linear, 'regressao-linear')

        print("Gráficos gerados com sucesso!")        
        
if __name__ == "__main__":

    data_atual = datetime.now().strftime("%Y-%m-%d")
    
    caminho = os.getcwd()
    caminho += f"//export//{data_atual}//"
        
    parametos = {
        "caminho_origem" : f"{caminho}",
        "arquivo" : "fipezap-serieshistoricas-formatado",
        "colunas" : ["Data", "Total"]
    }

    planilha : Planilha = Planilha(parametos)
    planilha.tabela = planilha.ler()

    grafico = Grafico(planilha.tabela)
    grafico.main()
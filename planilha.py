import pandas as pd
import os
import sys
from datetime import datetime

class Planilha:
    def __init__(self, parametros : dict):
        """Inicializa a planilha."""
        self.caminho_origem: str = parametros.get("caminho_origem")
        self.arquivo: str = parametros.get("arquivo")
        self.tabela: pd.DataFrame = pd.DataFrame()
        self.caminho_destino: str = parametros.get("caminho_destino")
        self.data_arquivo: str = datetime.now().strftime("%Y-%m-%d")
        self.aba: str = parametros.get("aba", None)
        self.colunas: list = parametros.get("colunas", None)

    def ler(self) -> pd.DataFrame:
        """Lê o arquivo da planilha.\n
        Se não for informada a aba da planilha, a primeira aba será lida.\n
        Se não for informado o cabeçalho, o padrão será o primeiro.\n
        Returns:
            `pd.DataFrame`: Tabela lida.
        """

        caminho = f"{self.caminho_origem}{self.arquivo}"

        if self.aba:
            return pd.read_excel(f"{caminho}", sheet_name=self.aba, usecols=self.colunas)
        
        return pd.read_excel(f"{caminho}", usecols=self.colunas)

    def converter_data(self, coluna : str) -> pd.Series:
        """Converte a coluna Data para o formato YYYY-MM-DD.\n
        Args:
            `coluna` (str): Nome da coluna a ser convertida.
        Returns:
            `pd.Series`: Coluna convertida.
        """

        return pd.to_datetime(self.tabela[coluna])

    def formatar_data_coluna(self, datas : pd.Series) -> pd.Series:
        """Formata as datas da coluna para o 
        formato YYYY-MM-DD.
        Args:
            `datas` (pd.Series): Coluna com as datas a serem formatadas.
        Returns:
            `pd.DataFrame`: Coluna formatada.
        """

        return datas.dt.strftime("%Y-%m-%d")

    def validar_duplicados(self, coluna : str) -> pd.DataFrame:
        """Valida se há valores duplicados em uma coluna.
        Args:
            `coluna` (str): Nome da coluna a ser validada.
        Returns:
            `True` (bool): Se houver valores duplicados.
            `False` (bool): Se não houver valores duplicados.
        """
        
        duplicados = self.tabela[coluna].duplicated()
        return duplicados.any()
    
    def remover_duplicados(self, coluna : str) -> pd.DataFrame:
        """Remove valores duplicados em uma coluna,
        mantendo a primeira ocorrência."""

        self.tabela.drop_duplicates(subset=[coluna], keep="first")
            
    def exportar(self, nome=None) -> None:
        """Exporta a tabela para um arquivo Excel."""
        
        caminho = f"{self.caminho_destino}/{self.data_arquivo}"
        
        if not os.path.exists(caminho):
            os.makedirs(caminho)

        arquivo = f"{nome}.xlsx" if nome \
            else f"{self.arquivo}-formatado.xlsx"

        self.tabela.to_excel(f"{caminho}\\{arquivo}", index=False)
    
    def exibir(self) -> None:
        """Exibe a tabela."""
        print(self.tabela)

if __name__ == '__main__':
    try:
        caminho = os.getcwd()
        
        parametos = {
            "caminho_origem" : f"{caminho}\\import\\",
            "arquivo" : "fipezap-serieshistoricas.xlsx",
            "caminho_destino" : f"{caminho}\\export\\",
            "aba" : "Índice FipeZAP",
            "colunas" : ["Data", "Total"]
        }

        planilha = Planilha(parametos)
        planilha.tabela = planilha.ler()
        print(planilha.tabela.head())
        planilha.exibir()
        
        datas = planilha.converter_data("Data")
        planilha.formatar_data_coluna("Data", datas)

        tem_duplicidade = planilha.validar_duplicados("Data")
        if tem_duplicidade:
            planilha.remover_duplicados("Data")

        planilha.exportar()

    except Exception as exc:
        erro = f"Erro: {sys.exc_info()[0]}\n"
        erro += f"Descrição: {sys.exc_info()[1]}\n"
        erro += f"Linha: {sys.exc_info()[2].tb_lineno}\n"
        erro += f"Exceção: {exc}"
        print(erro)

import pandas as pd
import os
import sys
from datetime import datetime

class Planilha:
    """Classe contendo as operações de leitura, conversão e exportação\n
    de planilhas Excel.\n
        Args:
            `parametros` (dict): Dicionário com os parâmetros da planilha.
        Attributes:
            `caminho_origem` (str): Caminho da planilha a ser lida.
            `arquivo` (str): Nome do arquivo da planilha a ser lida.
            `tabela` (pd.DataFrame): Tabela lida da planilha.
            `caminho_destino` (str): Caminho da pasta de destino da planilha.
            `data_arquivo` (str): Data atual no formato YYYY-MM-DD.
            `aba` (str): Nome da aba da planilha a ser lida.
            `colunas` (list): Lista com as colunas a serem lidas da planilha."""
    
    def __init__(self, parametros : dict):
        self.caminho_origem: str = parametros.get("caminho_origem")
        self.arquivo: str = parametros.get("arquivo")
        self.tabela: pd.DataFrame = pd.DataFrame()
        self.caminho_destino: str = parametros.get("caminho_destino")
        self.data_arquivo: str = datetime.now().strftime("%Y-%m-%d")
        self.aba: str = parametros.get("aba", None)
        self.colunas: list = parametros.get("colunas", None)
        self.quantidade : int = 0
        self.tipo_colunas : list = []
        self.formatado : bool = False

    def ler(self) -> pd.DataFrame:
        """Lê o arquivo da planilha.\n
        Se não for informada a aba da planilha, a primeira aba será lida.\n
        Returns:
            `pd.DataFrame`: Tabela lida."""

        if not self.formatado:
            caminho = f"{self.caminho_origem}{self.arquivo}.xlsx"

            if self.aba:
                return pd.read_excel(caminho, 
                        sheet_name=self.aba, 
                        skiprows=3,
                        usecols=self.colunas
                        )
            
            return pd.read_excel(caminho, 
                        usecols=self.colunas
                        )

        else:
            caminho = f"{self.caminho_destino}{self.data_arquivo}//{self.arquivo}-formatado.xlsx"

            return pd.read_excel(caminho, 
                        usecols=self.colunas
                        ) 

    def converter_data(self, coluna : str) -> pd.Series:
        """Converte a data da coluna para o formato YYYY-MM-DD.\n
        Caso o valor da célula não seja uma data válida,\n
        será preenchida com `NaT` (Not a Time).\n
        Args:
            `coluna` (str): Nome da coluna a ser convertida.
        Returns:
            `pd.Series`: Coluna convertida."""

        return pd.to_datetime(self.tabela[coluna], errors="coerce")

    def formatar_data_coluna(self, datas : pd.Series) -> pd.Series:
        """Formata as datas da coluna para o formato YYYY-MM-DD.\n
        Caso o valor da célula não seja uma data válida,\n
        será preenchida com `NaT` (Not a Time).\n
        Args:
            `datas` (pd.Series): Coluna com as datas a serem formatadas.
        Returns:
            `pd.DataFrame`: Coluna formatada."""

        return datas.dt.strftime("%Y-%m-%d")

    def validar_duplicados(self, coluna : str) -> pd.DataFrame:
        """Valida se há valores duplicados em uma coluna.\n
        Args:
            `coluna` (str): Nome da coluna a ser validada.
        Returns:
            `True` (bool): Se houver valores duplicados.
            `False` (bool): Se não houver valores duplicados."""
        
        duplicados = self.tabela[coluna].duplicated()
        return duplicados.any()
    
    def remover_duplicados(self, coluna : str) -> pd.DataFrame:
        """Remove valores duplicados em uma coluna,
        mantendo a primeira ocorrência.\n
        Args:
            `coluna` (str): Nome da coluna a remover duplicados."""

        self.tabela.drop_duplicates(subset=[coluna], keep="first")

    def contar(self, coluna : str) -> int:
        """Conta a quantidade de elementos de uma coluna.\n
        Args:
            `coluna` (str): Nome da coluna para contar os elementos.
        Returns:
            `int`: Quantidade de elementos da coluna."""
        
        self.quantidade = self.tabela[coluna].count()
    
    def validar_tipo_colunas(self) -> pd.Series.dtypes:
        """Valida o tipo das colunas da tabela.\n
        Returns:
            `pd.Series.dtypes`: Tipos das colunas da tabela."""
        
        for tipo in self.tabela.dtypes:
            self.tipo_colunas.append(tipo)
            
    def exportar(self, nome=None) -> None:
        """Exporta a tabela para um arquivo Excel.\n
        Args:
            `nome` (str): Nome do arquivo a ser exportado. \n
            
            Se não informado `nome`, será utilizado o nome 
            do arquivo original com o sufixo `-formatado`."""
        
        caminho = f"{self.caminho_destino}/{self.data_arquivo}"
        
        if not os.path.exists(caminho):
            os.makedirs(caminho)

        arquivo = f"{nome}.xlsx" if nome \
            else f"{self.arquivo}-formatado.xlsx"

        self.tabela.to_excel(f"{caminho}//{arquivo}", index=False)
    
    def exibir(self) -> None:
        """Exibe a tabela."""
        print(self.tabela)
        print(f"Quantidade de elementos: {self.quantidade}")
        print(f"Tipos das colunas: {self.tipo_colunas}")

    def main(self) -> None:
        """Método principal para leitura, conversão e exportação da planilha."""

        self.tabela = self.ler()

        datas = self.converter_data(coluna="Data")
        self.tabela["Data"] = self.formatar_data_coluna(datas)

        tem_duplicidade = self.validar_duplicados(coluna="Data")
        
        if tem_duplicidade:
            self.remover_duplicados(coluna="Data")

        self.exportar()

        self.contar(coluna="Data")
        self.validar_tipo_colunas()
        self.exibir()

        self.formatado = True
        self.tabela = self.ler()

        print("Planilha lida e formatada com sucesso!")

if __name__ == '__main__':
    try:
        caminho = os.getcwd()
        
        parametos = {
            "caminho_origem" : f"{caminho}//import//",
            "arquivo" : "fipezap-serieshistoricas",
            "caminho_destino" : f"{caminho}//export//",
            "aba" : "Índice FipeZAP",
            "colunas" : ["Data", "Total"]
        }

        planilha = Planilha(parametos)
        planilha.main()

    except Exception as exc:
        erro = f"Erro: {sys.exc_info()[0]}\n"
        erro += f"Descrição: {sys.exc_info()[1]}\n"
        erro += f"Linha: {sys.exc_info()[2].tb_lineno}\n"
        erro += f"Exceção: {exc}"
        print(erro)

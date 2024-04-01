import os
import pandas
import numpy
import matplotlib.pyplot
from planilha import Planilha
from calculo import Calculo
from grafico import Grafico
from datetime import datetime
from time import time

def main():
    """Método principal do projeto Py-Sci.\n
    Instala as dependências necessárias, lê e processa os dados da planilha,
    calcula os valores estatísticos, gera os gráficos com os resultados
    e exporta o arquivo dos gráficos gerados."""

    tempo_execucao = time()
    instalar_dependencias()

    planilha : Planilha = Planilha({
        "caminho_origem": f"{caminho}//import//",
        "arquivo": "fipezap-serieshistoricas",
        "caminho_destino": f"{caminho}//export//",
        "aba": "Índice FipeZAP",
        "colunas": ["Data", "Total"]
    })

    planilha.main()
    calculo = Calculo(planilha.tabela)
    calculo.main()
    grafico = Grafico(planilha.tabela)
    grafico.main()

    tempo_execucao = time() - tempo_execucao
    print(f"Tempo de execução: {tempo_execucao:.2f}s")

def instalar_dependencias() -> None:
    """Instala as dependências necessárias para a execução do script.
    `Diretório`: install/
    `Arquivo`: requirements.txt
    """

    print("Instalando dependências...")
    os.system("pip install -r install/requirements.txt")

if __name__ == "__main__":
    data_atual = datetime.now().strftime("%Y-%m-%d")
    caminho = os.getcwd()
    main()
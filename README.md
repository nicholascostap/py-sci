# Projeto PySci - Tabela Histórica FipeZAP

Este é um projeto de Data Science que utiliza Python, Pandas e Seaborn para analisar a tabela histórica de preços de imóveis da FipeZAP.

## Descrição

O objetivo deste projeto é explorar e visualizar os dados da tabela histórica da FipeZAP, que contém informações sobre os preços de imóveis ao longo do tempo. Utilizaremos as bibliotecas Pandas e Seaborn para realizar análises estatísticas e criar visualizações gráficas.

## Funcionalidades

- Carregar os dados da tabela histórica da FipeZAP em um DataFrame do Pandas.
- Limpar e preparar os dados para análise.
- Realizar análises estatísticas, como média, mediana e desvio padrão dos preços dos imóveis.
- Obter o Coeficiente de Variância.
- Criar visualizações gráficas, como gráficos de linha e histogramas, para visualizar os padrões e tendências dos preços.

##### NICE-TO-HAVE: Análise preditiva para prever os preços futuros dos imóveis com base nos dados históricos e em modelos de Machine Learning.

## Requisitos

- Python 3.x
- Pandas
- Seaborn

## Instalação

1. Clone este repositório:
https://github.com/nicholascostap/py-sci.git

2. Execute o Prompt de Comandos no modo Administrador e instale as dependências do projeto com os comandos abaixo:
```bash
cd py-sci
cd install
pip install -r requirements.txt
```

3. Faça o download do arquivo da tabela "fipezap-serieshistoricas.xlsx"
no link abaixo:
https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx

4. Mova o arquivo para a pasta "import" do projeto.

5. Execute o arquivo "planilha.py" para extrair os dados da tabela histórica da FipeZAP.

6. Execute o arquivo "calculo.py" para realizar os cálculos estatísticos.

7. Execute o arquivo "grafico.py" para gerar as visualizações gráficas.
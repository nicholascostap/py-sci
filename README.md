# PySci
![PySci Image](./src/img/logo-py-sci.png)
### Tabela Histórica FipeZAP

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
- Matplotlib
- NumPy

## Instalação

1. Clone este repositório:
https://github.com/nicholascostap/py-sci.git

2. Faça o download do arquivo da tabela "fipezap-serieshistoricas.xlsx"
no link abaixo:
https://downloads.fipe.org.br/indices/fipezap/fipezap-serieshistoricas.xlsx

3. Mova o arquivo para a pasta "import" do projeto.

4. Execute o arquivo "main.py" para carregar, processar os dados, calcular
os dados estatistícos e gerar os gráficos.
Esse arquivo instala as dependências necessárias para a execução e 
irá chamar os arquivos "planilha.py", "calculo.py" e "grafico.py".

5. Os resultados serão exibidos no console e os gráficos serão salvos na pasta "export". O script gera uma pasta com a data da execução, por padrão.
Os gráficos gerados são:

- Gráfico de Distribuição Normal
- Gráfico Boxplot
- Gráfico de Indíce x Tempo

#### Observação: Importante executar o arquivo à partir do diretório raíz do projeto.
```bash
.\py-sci
```

## Execução Step-by-Step

### Caso deseje executar os arquivos individualmente, siga os passos abaixo:

1. Execute o arquivo "planilha.py" para extrair os dados da tabela histórica da FipeZAP.

2. Execute o arquivo "calculo.py" para realizar os cálculos estatísticos.

3. Execute o arquivo "grafico.py" para gerar as visualizações gráficas.

### Instalação de dependências
### Caso deseje criar um ambiente virtual para instalar as dependências, siga os passos abaixo:

1. Crie um ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
```bash
.\venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Autores
👤 **Nicholas Costa P.**
- GitHub: https://github.com/nicholascostap

👤 **Gyovanna Lima**
- GitHub: https://github.com/glsanto-s

👤 **Henrique Gil**
- GitHub: https://github.com/Henrique762

👤 **Rogério Lacerda**
- GitHub: https://github.com/Rogerio-Lacerda

👤 **Guilherme Silveira**
- GitHub: https://github.com/GuiiGhost

👤 **Gabrielly Venancio**
- GitHub: https://github.com/gabirelly-venancio

## 🤝 Contribuições

👤 **Cesar**
- Orientador

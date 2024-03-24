import pandas as pd
import os

class Table:
    def __init__(self, values : dict):
        self.path : str = values.get("path")
        self.file : str = values.get("file")

    def read(self) -> pd.DataFrame:
        """Lê o arquivo da planilha, à partir do caminho a ser lido
        e retorna um DataFrame Pandas."""
        return pd.read_excel(f"{self.path}{self.file}")

if __name__ == "__main__":
    
    values = {
        "path" : f"{os.getcwd()}\\import\\",
        "file" : "fipezap-serieshistoricas.xlsx"
    }

    table = Table(values)
    df = table.read()
    print(df.head())
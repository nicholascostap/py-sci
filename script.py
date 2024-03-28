import pandas as pd
import os

class Sheet:
    def __init__(self, values : dict):
        self.path : str = values.get("path")
        self.file : str = values.get("file")

    def read(self) -> pd.DataFrame:
        """Lê o arquivo da planilha, à partir do caminho a ser lido
        e retorna um DataFrame Pandas."""
        return pd.read_excel(f"{self.path}{self.file}")
    
    def get_variant_coefficient(self) -> float:
        """Obtém o coeficiente de variação da planilha."""

        data_frame = self.read()
        average = data_frame["Total"].mean()
        default_deviation = data_frame["Total"].std()

        return default_deviation / average

if __name__ == "__main__":
    
    values = {
        "path" : f"{os.getcwd()}\\py-sci\\import\\",
        "file" : "tabelaPooFormatada.xlsx"
    }

    sheet = Sheet(values)
    df = sheet.read()
    print(df.head())
import pandas as pd


class MarketData:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        self.df.set_index("Year/Stock", inplace=True)

    def get_years(self):
        return self.df.index.tolist()

    def get_assets(self):
        return self.df.columns.tolist()

    def get_returns(self, year):
        return self.df.loc[year].to_dict()
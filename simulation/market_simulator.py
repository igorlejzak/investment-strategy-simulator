import pandas as pd

class MarketSimulator:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path)
        self.df.set_index('Year/Stock', inplace=True)

    def get_available_years(self):
        return self.df.index.tolist()

    def get_returns_for_year(self, year):
        return self.df.loc[year].to_dict()
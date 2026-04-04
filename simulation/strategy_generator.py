import itertools

class StrategyGenerator:
    def get_all_paths(self, assets, num_periods):
        return list(itertools.product(assets, repeat=num_periods))
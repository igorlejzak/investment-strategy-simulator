from simulation.market_simulator import MarketSimulator
from game.game_engine import FinanceEngine
from simulation.strategy_generator import StrategyGenerator
import pandas as pd

def run_simulation():
    sim = MarketSimulator("data/returns_data.xlsx")
    engine = FinanceEngine()
    generator = StrategyGenerator()

    initial_capital = 10000.0
    years = sim.get_available_years()
    assets = list(sim.get_returns_for_year(years[0]).keys())

    print(f"Checking all possible strategies for {len(assets)} assets over {len(years)} periods...")
    all_paths = generator.get_all_paths(assets, len(years))
    print(f"Total strategies: {len(all_paths):,}")

    results = []

    for path in all_paths:
        capital = initial_capital
        for i, year in enumerate(years):
            ret = sim.get_returns_for_year(year)[path[i]]
            capital = engine.calculate_new_capital(capital, ret)
        results.append({"path": path, "final_capital": capital})

    results_df = pd.DataFrame(results)

    best = results_df.loc[results_df["final_capital"].idxmax()]
    worst = results_df.loc[results_df["final_capital"].idxmin()]

    print("\n===== RESULTS =====")
    print(f"Best strategy:  {best['path']}")
    print(f"Final capital:  ${best['final_capital']:,.2f}")
    print(f"\nWorst strategy: {worst['path']}")
    print(f"Final capital:  ${worst['final_capital']:,.2f}")
    print(f"\nAverage capital: ${results_df['final_capital'].mean():,.2f}")
    print(f"Total strategies checked: {len(results_df):,}")

if __name__ == "__main__":
    run_simulation()
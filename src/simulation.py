import itertools
import pandas as pd
from src.game import calculate_capital


def run_simulation(market):
    initial_capital = 10000.0
    years = market.get_years()
    assets = market.get_assets()

    all_paths = list(itertools.product(assets, repeat=len(years)))
    print(f"Checking all {len(all_paths):,} possible strategies...\n")

    results = []

    for path in all_paths:
        capital = initial_capital
        for i, year in enumerate(years):
            ret = market.get_returns(year)[path[i]]
            capital = calculate_capital(capital, ret)
        results.append({"path": path, "final_capital": capital})

    df = pd.DataFrame(results)
    best = df.loc[df["final_capital"].idxmax()]
    worst = df.loc[df["final_capital"].idxmin()]

    print("===== RESULTS =====")
    print(f"Best strategy:   {best['path']}")
    print(f"Final capital:   ${best['final_capital']:,.2f}")
    print(f"\nWorst strategy:  {worst['path']}")
    print(f"Final capital:   ${worst['final_capital']:,.2f}")
    print(f"\nAverage capital: ${df['final_capital'].mean():,.2f}")
    print(f"Strategies checked: {len(df):,}")
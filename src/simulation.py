import itertools
import pandas as pd
import matplotlib.pyplot as plt
import os
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
        capitals = [capital]
        for i, year in enumerate(years):
            ret = market.get_returns(year)[path[i]]
            capital = calculate_capital(capital, ret)
            capitals.append(capital)
        results.append({
            "path": path,
            "final_capital": capital,
            "capitals": capitals,
        })

    df = pd.DataFrame(results)
    df_sorted = df.sort_values("final_capital", ascending=False).reset_index(drop=True)

    best   = df_sorted.iloc[0]
    good   = df_sorted.iloc[len(df_sorted) // 4]
    median = df_sorted.iloc[len(df_sorted) // 2]
    bad    = df_sorted.iloc[3 * len(df_sorted) // 4]
    worst  = df_sorted.iloc[-1]

    print("===== RESULTS =====")
    print(f"Best strategy:    {best['path']}")
    print(f"Final capital:    ${best['final_capital']:,.2f}")
    print(f"\nWorst strategy:   {worst['path']}")
    print(f"Final capital:    ${worst['final_capital']:,.2f}")
    print(f"\nAverage capital:  ${df['final_capital'].mean():,.2f}")
    print(f"Strategies checked: {len(df):,}")

    _save_excel(years, best, good, median, bad, worst, df)
    _plot_results(years, df_sorted, best, worst, initial_capital)


def _save_excel(years, best, good, median, bad, worst, df):
    os.makedirs("results", exist_ok=True)
    periods = [f"{y}-{y+5}" for y in years]

    rows = []
    for scenario, label in [(best, "Best"), (good, "Good"),
                             (median, "Median"), (bad, "Bad"), (worst, "Worst")]:
        row = {"Scenario": label, "Final Capital ($)": round(scenario["final_capital"], 2)}
        for i, period in enumerate(periods):
            row[period] = scenario["path"][i]
        rows.append(row)

    summary_df = pd.DataFrame(rows)
    summary_df.to_excel("results/simulation_results.xlsx", index=False)
    print("\nResults saved to results/simulation_results.xlsx")


def _plot_results(years, df_sorted, best, worst, initial_capital):
    x_labels = ["Start"] + [str(y) for y in years]
    x = list(range(len(x_labels)))

    plt.figure(figsize=(14, 7))

    for _, row in df_sorted.iterrows():
        plt.plot(x, row["capitals"], color="gray", alpha=0.02, linewidth=0.3)

    plt.plot(x, worst["capitals"], color="red", linewidth=2,
             label=f"Worst: ${worst['final_capital']:,.0f}")
    plt.plot(x, best["capitals"], color="green", linewidth=2,
             label=f"Best: ${best['final_capital']:,.0f}")

    plt.axhline(y=initial_capital, color="blue", linestyle="--",
                linewidth=1.5, label=f"Starting capital: ${initial_capital:,.0f}")

    plt.yscale("log")
    plt.xticks(x, x_labels, fontsize=9)
    plt.ylabel("Capital ($) — log scale")
    plt.title("Investment Strategy Simulation — All Possible Paths")
    plt.legend(loc="upper left")
    plt.gca().yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"${v:,.0f}")
    )
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    os.makedirs("results", exist_ok=True)
    plt.savefig("results/simulation_chart.png", dpi=150)
    plt.show()
    print("Chart saved to results/simulation_chart.png")
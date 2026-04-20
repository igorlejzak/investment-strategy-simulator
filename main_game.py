from simulation.market_simulator import MarketSimulator
from game.game_engine import FinanceEngine

def run_game():
    sim = MarketSimulator("data/returns_data.xlsx")
    engine = FinanceEngine()

    capital = 10000.0
    years = sim.get_available_years()

    print("--- INVESTMENT STRATEGY GAME ---")
    print("Goal: Pick one asset every 5 years and grow your capital.")
    print("You can only see past data - future returns are hidden!")

    for i, year in enumerate(years):
        print("\n" + "=" * 50)
        print(f"YEAR: {year}")
        print(f"CAPITAL: ${capital:,.2f}")
        print("=" * 50)

        if i > 0:
            print("\n[ HISTORICAL DATA ]")
            print(sim.df.iloc[:i].to_string())
        else:
            print("\n[ NO HISTORICAL DATA YET - FIRST ROUND ]")

        current_returns = sim.get_returns_for_year(year)
        assets = list(current_returns.keys())

        print(f"\nChoose your asset for {year}-{year+5}:")
        print("Options: " + ", ".join(assets))

        choice = ""
        while choice not in assets:
            choice = input("Your choice: ").strip()

        ret = current_returns[choice]
        capital = engine.calculate_new_capital(capital, ret)

        print(f"\n>>> {choice} returned {ret * 100:.2f}% this period")

    print("\n" + "#" * 50)
    print("GAME OVER")
    print(f"FINAL BALANCE: ${capital:,.2f}")
    print("#" * 50)

if __name__ == "__main__":
    run_game()
    run_game()
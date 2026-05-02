def calculate_capital(capital, return_rate):
    return capital * (1 + return_rate)


def run_game(market):
    capital = 10000.0
    years = market.get_years()

    print("--- INVESTMENT STRATEGY GAME ---")
    print("Pick one asset every 5 years and grow your $10,000.")
    print("You can only see past data - future returns are hidden.\n")

    for i, year in enumerate(years):
        print("=" * 50)
        print(f"YEAR: {year}  |  CAPITAL: ${capital:,.2f}")
        print("=" * 50)

        if i > 0:
            print("\n[ HISTORICAL DATA ]")
            history = market.df.iloc[:i].copy()
            history_pct = history.applymap(lambda x: f"{x*100:+.1f}%")
            print(history_pct.to_string())
        else:
            print("\n[ NO HISTORICAL DATA YET - FIRST ROUND ]")

        assets = list(market.get_returns(year).keys())
        returns = market.get_returns(year)

        print(f"\nChoose your asset for {year}-{year + 5}:")
        for idx, asset in enumerate(assets, 1):
            print(f"  {idx}. {asset}")

        choice_idx = None
        while choice_idx is None:
            try:
                val = int(input("Your choice (number): ").strip())
                if 1 <= val <= len(assets):
                    choice_idx = val - 1
                else:
                    print(f"Enter a number between 1 and {len(assets)}")
            except ValueError:
                print(f"Enter a number between 1 and {len(assets)}")

        choice = assets[choice_idx]
        ret = returns[choice]
        capital = calculate_capital(capital, ret)

        print(f"\n>>> {choice} returned {ret * 100:+.1f}% this period\n")

    print("#" * 50)
    print("GAME OVER")
    print(f"FINAL BALANCE: ${capital:,.2f}")
    print("#" * 50)
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
            print(market.df.iloc[:i].to_string())
        else:
            print("\n[ NO HISTORICAL DATA YET - FIRST ROUND ]")

        assets = list(market.get_returns(year).keys())
        print(f"\nChoose your asset for {year}-{year + 5}:")
        print("Options: " + ", ".join(assets))

        choice = ""
        while choice not in assets:
            choice = input("Your choice: ").strip()

        ret = market.get_returns(year)[choice]
        capital = calculate_capital(capital, ret)

        print(f"\n>>> {choice} returned {ret * 100:.2f}% this period\n")

    print("#" * 50)
    print("GAME OVER")
    print(f"FINAL BALANCE: ${capital:,.2f}")
    print("#" * 50)
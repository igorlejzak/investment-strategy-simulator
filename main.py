import argparse
from src.market_data import MarketData
from src.game import run_game
from src.simulation import run_simulation


def main():
    parser = argparse.ArgumentParser(description="Investment Strategy Simulator")
    parser.add_argument("mode", choices=["game", "simulation"], help="Run mode")
    args = parser.parse_args()

    market = MarketData("data/returns_data.xlsx")

    if args.mode == "game":
        run_game(market)
    elif args.mode == "simulation":
        run_simulation(market)


if __name__ == "__main__":
    main()
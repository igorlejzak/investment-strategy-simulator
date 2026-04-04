# Investment Strategy Simulator

A two-part project built around a simple question:
"How good are my investment decisions compared to all possible strategies?"

## How it works

**Part 1 - The Game (`main_game.py`)**
The player starts with $10,000 and picks one asset every 5 years.
Only historical data is visible - future returns are hidden.
Available assets: S&P 500, NASDAQ, Gold, Oil, US 10Y Treasury.

**Part 2 - The Simulation (`main_simulation.py`)**
After the game, the program runs a brute-force simulation of every possible
strategy (all combinations of assets across all periods) and shows
which path was the best and which was the worst.
This way you can see exactly how your decisions compared to the optimal strategy.

## How to run
```bash
# Play the game
pip install -r requirements.txt
python main_game.py

# Run the full brute-force simulation
python main_simulation.py
```

## Tech
Python, Pandas, itertools
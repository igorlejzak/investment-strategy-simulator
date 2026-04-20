# Investment Strategy Simulator

A Python project built to explore how different asset allocation strategies
perform over time using historical market data.

## How it works

The project has two modes:

**Game mode** — the player starts with $10,000 and picks one asset every 5 years.
Only past data is visible, future returns are hidden. At the end you see your final balance.

**Simulation mode** — brute-force analysis of every possible investment strategy
across all periods. Finds the best and worst performing paths out of all combinations.

## Assets
S&P 500, NASDAQ, Gold, Oil, US 10Y Treasury

## Usage
```bash
pip install -r requirements.txt

python main.py game        # play the interactive game
python main.py simulation  # run full brute-force analysis
```

## Project structure
```
src/
  market_data.py   - loads historical returns from Excel
  game.py          - interactive game logic
  simulation.py    - brute-force strategy analysis
data/
  returns_data.xlsx
docs/
  description.md
main.py            - entry point, argument parsing
```

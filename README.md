# Investment Strategy Simulator

Python project for testing investment decisions against historical market data (1990–2025).

## Two modes

**Game** — start with $10,000, pick one asset every 5 years with only past data visible.
Choose by number, see returns in % after each period.

**Simulation** — brute-force all 78,125 possible strategies, visualize every path
on a log-scale chart, and export best/worst/median results to Excel.

## Assets
S&P 500, NASDAQ, Gold, Emerging Markets, Real Estate

## Usage
```bash
pip install -r requirements.txt
python main.py game
python main.py simulation
```

## Structure
```
src/          market data, game logic, simulation and visualization
data/         historical returns (Excel, 1990-2025)
results/      generated charts and Excel output (gitignored)
main.py       entry point with argparse
```

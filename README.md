# Investment Strategy Simulator

Python project that lets you test your investment decisions against historical market data.

## Two modes

**Game** — start with $10,000, pick one asset every 5 years with only past data visible.

**Simulation** — brute-force all possible strategies and find the best and worst outcome.

## Assets
S&P 500, NASDAQ, Gold, Oil, Real Estate

## Usage
```bash
pip install -r requirements.txt
python main.py game
python main.py simulation
```

## Structure
```
src/          market data, game logic, simulation
data/         historical returns (Excel)
main.py       entry point
```

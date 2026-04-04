# Bank Liquidity Simulation

A Python project I built to learn more about how banks manage liquidity risk.

The program simulates how a bank's liquidity buffer changes over 90 days,
using Monte Carlo methods to model random daily deposits and withdrawals.
I wanted to see how many scenarios end up below the minimum buffer threshold
and what the best and worst case paths look like.

## What it does
- Loads deposit data from a CSV file
- Runs 100 Monte Carlo simulations of daily cash flows
- Tracks the liquidity buffer over time for each scenario
- Highlights the best and worst performing paths on a chart
- Shows the minimum required buffer (20% of total deposits)

## How to run
```bash
pip install -r requirements.txt
python main.py
```

## Tech
Python, NumPy, Pandas, Matplotlib
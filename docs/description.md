## How it works

The project has two modes controlled via command line argument:

- `game` — interactive mode where the player picks assets year by year
- `simulation` — brute-force mode that checks every possible strategy

The `main.py` file only handles argument parsing and calls the appropriate module.
All logic lives in `src/`.
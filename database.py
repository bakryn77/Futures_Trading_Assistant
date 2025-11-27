import json        # Lets us read/write JSON files (like mini-databases)
import os          # Lets us check if the file exists before opening it


# This is the filename where all your saved trades will live.
# You can treat this like your futures assistant's "database".
DB_FILE = "trades.json"


def load_trades():
    """
    Load all stored trades from the JSON file.
    Returns a Python list.
    """

    # If the file doesn't exist yet (first time running the program)
    # return an empty list instead of crashing.
    if not os.path.exists(DB_FILE):
        return []

    # Open the file and read its content.
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            # Convert JSON text → Python list
            return json.load(f)
        except json.JSONDecodeError:
            # If the file is corrupt or empty, return empty list.
            return []


def save_trades(trades: list):
    """
    Save the ENTIRE list of trades to the JSON file.
    This overwrites the old file with updated content.
    """

    # Open the file in write mode ("w")
    # indent=2 makes the JSON pretty and readable.
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(trades, f, indent=2)


def add_trade(trade: dict):
    """
    Add one new trade to the list and save it.
    - Loads current trades
    - Appends new trade
    - Saves everything again

    Example of a trade:
    {
        "symbol": "MES",
        "direction": "long",
        "pnl": 150.25,
        "entry": 4820.5,
        "exit": 4823.75
    }
    """

    # Step 1: Load everything that was saved so far
    trades = load_trades()

    # Step 2: Add the new trade to the list
    trades.append(trade)

    # Step 3: Save everything back to trades.json
    save_trades(trades)

    # Useful print so you can see it worked
    print(f"[DB] Stored trade: {trade}")


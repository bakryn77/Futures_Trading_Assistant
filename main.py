# These import functions from your storage/database.py file.
# They allow main.py to use your database.
from storage.database import add_trade, load_trades


def show_menu():
    """
    Print the main menu for the Futures Assistant V0.
    Now includes automatic scraping with Selenium.
    """
    print("\n==== Futures Assistant V0 ====")
    print("1. Scrape trades automatically from Topstep")
    print("2. View all stored trades")
    print("3. Add a trade manually")
    print("4. Exit")


def manual_trade_input():
    """
    This function asks the user for information about a trade.
    It collects the data, builds a trade dictionary,
    and sends it to add_trade() to save it.
    """

    print("\nEnter trade details:")

    # Ask user for each part of the trade
    symbol = input("Symbol (MES/NQ/etc): ")
    direction = input("Direction (long/short): ")

    # pnl and entry/exit need to be numbers → convert using float()
    pnl = float(input("PnL ($): "))
    entry = float(input("Entry price: "))
    exit_price = float(input("Exit price: "))

    # Build the trade as a Python dictionary
    trade = {
        "symbol": symbol.upper(),      # Convert symbol to uppercase (e.g. mes → MES)
        "direction": direction.lower(),# Convert long/SHORT to lowercase
        "pnl": pnl,
        "entry": entry,
        "exit": exit_price
    }

    # Save the trade using the database function
    add_trade(trade)


def main():
    """
    This function runs in a loop, showing the menu and handling choices.
    It is the "main program" for your app.
    """

    while True:  # Loop forever until the user chooses Exit
        show_menu()

        # Ask the user what they want to do
        choice = input("Choose an option: ")

        # User chooses to add a trade
        if choice == "1":
            manual_trade_input()

        # User wants to view saved trades
        elif choice == "2":
            trades = load_trades()    # Load list of trades
            print("\n=== Stored Trades ===")
            for t in trades:          # Loop through each trade
                print(t)

        # Quit the program
        elif choice == "3":
            print("Goodbye.")
            break  # This ends the while loop → ends the program

        # Anything else is invalid
        else:
            print("Invalid option. Try again.")


# This line tells Python to run main() ONLY if the file is run directly.
# (It prevents code from running accidentally when importing.)
if __name__ == "__main__":
    main()

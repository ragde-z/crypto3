# backtesting.py
import pandas as pd

def run_backtest(data):
    # Initialize variables
    initial_balance = 10000  # Starting capital in USD
    balance = initial_balance
    position = 0  # Tracks whether we are in a trade (1 = bought, 0 = not in a trade)
    entry_price = 0
    num_trades = 0
    wins = 0
    losses = 0

    # Iterate through the data to simulate trades
    for i in range(1, len(data)):
        if data['Prediction'].iloc[i] == 1 and position == 0:  # Buy signal
            entry_price = data['Close'].iloc[i]
            position = 1
            num_trades += 1
            print(f"Buy at {entry_price}")

        elif data['Prediction'].iloc[i] == 0 and position == 1:  # Sell signal
            exit_price = data['Close'].iloc[i]
            position = 0
            profit = exit_price - entry_price

            # Track win/loss
            if profit > 0:
                wins += 1
            else:
                losses += 1

            balance += profit
            print(f"Sell at {exit_price} | Profit: {profit:.2f}")

    # Calculate final performance metrics
    total_return = ((balance - initial_balance) / initial_balance) * 100
    win_rate = wins / num_trades if num_trades > 0 else 0

    print(f"Final Balance: ${balance:.2f}")
    print(f"Total Return: {total_return:.2f}%")
    print(f"Win Rate: {win_rate:.2f}")

    return {
        'initial_balance': initial_balance,
        'final_balance': balance,
        'total_return': total_return,
        'win_rate': win_rate
    }

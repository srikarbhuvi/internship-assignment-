import pandas as pd
import numpy as np

def calculate_scalping_entry_exit(prices, scalp_percentage, stop_loss_percentage):
    """
    Calculate the entry and exit points for scalping trades based on price fluctuations and stop loss.

    Args:
        prices (list): A list of historical prices in chronological order.
        scalp_percentage (float): The desired scalp percentage for profit taking.
        stop_loss_percentage (float): The desired stop loss percentage for risk management.

    Returns:
        entry_points (list): A list of entry points for scalping trades.
        exit_points (list): A list of corresponding exit points for the scalping trades.
    """
    entry_points = []
    exit_points = []

    for i in range(len(prices)-1):
        entry_price = prices[i]
        stop_loss_price = entry_price * (1 - stop_loss_percentage)
        exit_price = entry_price * (1 + scalp_percentage)

        # Check if stop loss is triggered before exit
        if np.min(prices[i+1:]) < stop_loss_price:
            exit_price = stop_loss_price

        entry_points.append(entry_price)
        exit_points.append(exit_price)

    return entry_points, exit_points

def calculate_strategy(prices, scalp_percentage, stop_loss_percentage, moving_average_period):
    """
    Calculate the combined strategy of scalping and moving averages.

    Args:
        prices (list): A list of historical prices in chronological order.
        scalp_percentage (float): The desired scalp percentage for profit taking.
        stop_loss_percentage (float): The desired stop loss percentage for risk management.
        moving_average_period (int): The period for the moving average calculation.

    Returns:
        entry_points (list): A list of entry points for the combined strategy.
        exit_points (list): A list of corresponding exit points for the combined strategy.
    """
    entry_points = []
    exit_points = []

    # Calculate moving averages
    moving_averages = pd.Series(prices).rolling(window=moving_average_period).mean().values

    for i in range(len(prices)-1):
        if prices[i] > moving_averages[i]:
            # Apply scalping strategy
            entry_price, exit_price = calculate_scalping_entry_exit(prices[i:], scalp_percentage, stop_loss_percentage)
            entry_points.extend(entry_price)
            exit_points.extend(exit_price)

    return entry_points, exit_points

# Example usage:

    # Historical prices (replace with actual values)
prices = [100, 105, 102, 108, 107, 110, 112, 115]

    # Desired scalp percentage
scalp_percentage = 0.02

    # Desired stop loss percentage
stop_loss_percentage = 0.01

    # Moving average period
moving_average_period = 5

    # Calculate entry and exit points for the combined strategy
entry_points, exit_points = calculate_strategy(prices, scalp_percentage, stop_loss_percentage, moving_average_period)

    # Print the entry and exit points
print("Entry Points:")
print(entry_points)
print("\nExit Points:")
print(exit_points)

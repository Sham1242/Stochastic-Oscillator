import numpy as np

def calculate_stochastic_oscillator(high_prices, low_prices, close_prices, period=14):
    # Calculate the highest and lowest prices over the given period
    highest_high = np.max(high_prices[-period:])
    lowest_low = np.min(low_prices[-period:])

    # Calculate the %K and %D values
    current_close = close_prices[-1]
    %K = 100 * (current_close - lowest_low) / (highest_high - lowest_low)
    %D = np.mean(%K[-3:])  # SMA of last 3 %K values

    return %K, %D

# Example usage
# Replace the 'high_prices', 'low_prices', and 'close_prices' lists with your actual stock price data
# Make sure the lists contain the prices for the last hour

high_prices = [100, 110, 95, 105, 115, 125, 130, 135, 140, 120, 110, 105, 100, 95, 90]
low_prices = [90, 100, 85, 95, 105, 115, 120, 125, 130, 110, 100, 95, 90, 85, 80]
close_prices = [95, 105, 90, 100, 110, 120, 125, 130, 135, 115, 105, 100, 95, 90, 85]

%K, %D = calculate_stochastic_oscillator(high_prices, low_prices, close_prices)
print("Current %K:", %K)
print("Current %D:", %D)

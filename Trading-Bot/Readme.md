# Alpaca Trading Strategy

This is a Python script that implements a trading strategy using the Alpaca API. The strategy involves selecting a universe of stocks, ranking them based on price changes, and rebalancing the portfolio accordingly. The script will automatically execute buy and sell orders on the Alpaca platform.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Required Python packages (see `requirements.txt`)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/salted0dreams/alpaca-trading-strategy.git
    ```


2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```


3. Open the `main.py` file and replace the placeholder values for `API_KEY` and `API_KEY_SECRET` with your Alpaca API credentials.


4. Run the script:

    ```bash
    python main.py
    ```

Certainly! Here's the code for the README.md file:

markdown

# Alpaca Trading Strategy

This is a Python script that implements a trading strategy using the Alpaca API. The strategy involves selecting a universe of stocks, ranking them based on price changes, and rebalancing the portfolio accordingly. The script will automatically execute buy and sell orders on the Alpaca platform.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Required Python packages (see `requirements.txt`)

## Getting Started

1. Clone the repository:

git clone https://github.com/your-username/alpaca-trading-strategy.git

markdown


2. Install the required Python packages:

pip install -r requirements.txt

css


3. Open the `main.py` file and replace the placeholder values for `API_KEY` and `API_KEY_SECRET` with your Alpaca API credentials.

4. Customize the stock universe and position size according to your preferences:

```
    python main.py
```


### Strategy Overview

The trading strategy implemented in this script follows these steps:

    Connect to the Alpaca API using the provided API credentials.
    Define the stock universe and initialize portfolio variables.
    Wait for the market to open.
    Continuously monitor the market and rebalance the portfolio.
    Close all positions before the market closes.
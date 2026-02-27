# Cryptocurrency Market Data Fetcher (CoinGecko API)
Project Overview:

This project fetches real-time cryptocurrency market data using the public API from CoinGecko.

It retrieves:

Top 10 cryptocurrencies by market capitalization

Current price in INR

24-hour high and low prices

24-hour price change percentage

Top 5 gainers

This project demonstrates:

API integration

JSON data processing

Data manipulation using Pandas

Real-time financial data analysis

# Features

Fetches live cryptocurrency data

Converts JSON response to Pandas DataFrame

Displays structured market table

Identifies top 5 daily gainers

Simple, clean, modular code structure

# Tech Stack

Python

Requests (API calls)

Pandas (Data processing)

# Project Structure
crypto_market_fetcher/
│
├── crypto_fetcher.py
└── README.md
# Installation

Install required dependencies:

pip install requests pandas


Sorted by highest 24-hour percentage growth.

# How It Works
1️. Fetch Data

The script calls:

https://api.coingecko.com/api/v3/coins/markets

Parameters:

vs_currency=INR

order=market_cap_desc

per_page=10

page=1

2️. Process Data

The JSON response is converted into a Pandas DataFrame and filtered to include:

name

current_price

high_24h

low_24h

price_change_percentage_24h

3️. Analyze Data

Displays full table

Uses nlargest() to find top 5 gainers

# Real-World Applications

Crypto portfolio tracking

Financial dashboards

Trading analysis tools

Investment monitoring systems

Market research

# Possible Improvements

Add live auto-refresh every 60 seconds

Save data to CSV

Create visualizations (Matplotlib / Seaborn)

Build Streamlit dashboard

Add top losers analysis

Add historical price tracking

Deploy as web app

# Future Enhancements

Multi-currency support (USD, EUR, etc.)

Email alerts for price spikes

Telegram bot integration

Predictive modeling (price forecasting)

Integration with Binance API

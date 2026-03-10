# 📈 Python Stock Price Alert Tracker

## Overview

This project is a Python automation tool that monitors stock prices and sends an email alert when a stock reaches a user-defined target price.

The script uses the Yahoo Finance API through the `yfinance` library to retrieve current stock prices. When a target price is reached, an email notification is automatically sent to the user.

The program also keeps track of previously triggered alerts to prevent duplicate notifications.

This project demonstrates practical Python automation, API usage, file handling, and task scheduling.

---



#### Demo Output

Example terminal output when the script runs:

```
BCO current price: $125.83
FHLC current price: $75.12
WEN current price: $10.02

🚨 ALERT: WEN hit your target!
```

Example alert email:

```
Subject: Stock Alert: WEN

WEN has reached your target price!

Current Price: $10.02
Target Price: $10.00
```
 Features

* 📊 Retrieves live stock prices using Yahoo Finance
* 🚨 Sends email alerts when a target price is reached
* 📁 Prevents duplicate alerts using a persistent alert log
* 📝 Logs every script execution to verify automation
* ⚡ Designed to run automatically using Windows Task Scheduler

---

## Technologies Used

* Python
* yfinance API
* SMTP email automation
* File handling
* Windows Task Scheduler

---

## How It Works

1. The script loads a list of stock symbols and target prices.
2. The program retrieves the current stock price using the `yfinance` API.
3. If the current price meets or exceeds the target:

   * An email alert is sent.
   * The stock is recorded in a log to prevent duplicate alerts.
4. Each time the script runs, a timestamp is written to a log file.

---

## Project Structure

```
stock-price-alert-tracker
│
├── watchlist.py
├── alerted_stocks.txt
├── run_log.txt
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/stock-price-alert-tracker.git
cd stock-price-alert-tracker
```

Create a virtual environment:

```
python -m venv stockenv
```

Activate the environment:

Windows:

```
stockenv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Requirements

Create a `requirements.txt` file with:

```
yfinance
```

Then install using:

```
pip install -r requirements.txt
```

---

## Running the Script

```
python watchlist.py
```

The script will check each stock and send an email if a target price has been reached.

---

## Automation

This project is designed to run automatically using Windows Task Scheduler.

Example schedule:

* Run once per day at **1:00 PM**

---

## Future Improvements

* CSV-based watchlists
* Market-hours filtering
* Daily summary emails
* Portfolio performance tracking
* Web dashboard for stock monitoring

---

## Disclaimer

This project is for educational and demonstration purposes only and should not be used as financial advice.


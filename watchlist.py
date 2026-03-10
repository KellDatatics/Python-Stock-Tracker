#Create a stock watch list

import yfinance as yf
import smtplib
import os
from email.message import EmailMessage
from datetime import datetime

with open("run_log.txt", "a") as log:#create a log that shows the task was ran
    log.write(f"Stock tracker ran at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")#the log runs when the script executes even if it crashes i know it started

def send_email(symbol, price, target):#email function, the subject and details

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_ADDRESS")
   
    msg = EmailMessage()
    msg["Subject"] = f"Stock Alert: {symbol}"
    msg["From"] = sender
    msg["To"] = recipient

    msg.set_content(
        f"{symbol} has reached your target price!\n\n"
        f"Current Price: ${price:.2f}\n"
        f"Target Price: ${target:.2f}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)



stocks = {
    "BCO": 130,
    "FHLC": 77,
    "FSMAX": 106,
    "HNST": 3,
    "IRT": 20,
    "WEN": 10
}


try:
    with open("alerted_stocks.txt", "r") as file:#checking to see if the email was already sent
        alerted_stocks = file.read().splitlines()#read on the alerted_stocks list
except FileNotFoundError:
    alerted_stocks = []


for symbol, target_price in stocks.items():

    ticker = yf.Ticker(symbol)

    try:#prevent crashes
        current_price = ticker.fast_info["lastPrice"]

        print(f"{symbol} current price: ${current_price:.2f}")

        if current_price >= target_price:

            if symbol not in alerted_stocks:#checking the alerted list

                print(f"🚨 ALERT: {symbol} hit your target!")#send alert

                send_email(symbol, current_price, target_price)#what to send in email

                with open("alerted_stocks.txt", "a") as file:
                    file.write(symbol + "\n")#write on the alerted_stocks file

            else:
                print(f"{symbol} already alerted.")

    except Exception:
        print(f"Could not fetch price for {symbol}")

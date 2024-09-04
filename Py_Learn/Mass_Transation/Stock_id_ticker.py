import requests
import csv

def fetch_stock_ids():
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=json'
    response = requests.get(url)
    data = response.json()

    stock_list = data['data']
    with open('stock_id.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Stock ID', 'Stock Name'])
        for stock in stock_list:
            writer.writerow([stock[0], stock[1]])

fetch_stock_ids()

import yfinance as yf


def fetch_stock_details():
    with open('stock_id.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            stock_id = row[0]
            stock = yf.Ticker(stock_id + '.TW')
            info = stock.info
            print(f"Stock ID: {stock_id}")
            print(f"Stock Name: {row[1]}")
            print(f"Market Cap: {info.get('marketCap')}")
            print(f"PE Ratio: {info.get('trailingPE')}")
            print(f"Dividend Yield: {info.get('dividendYield')}")
            print("------")

fetch_stock_details()

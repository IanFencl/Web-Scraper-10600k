import requests
from bs4 import BeautifulSoup
import schedule
import time

def job():
    URL = 'https://www.nowinstock.net/computers/processors/intel/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='tr50491')
    stocks = results.find_all('td', class_='stockStatus')
    for stock in stocks:
        stock_elem = results.find('td', class_='stockStatus')
        if None in stock:
            continue
        if (stock_elem.text == "In Stock"):
            print('IN STOCK AT AMAZON\n')
    results = soup.find(id='tr50490')
    stocks = results.find_all('td', class_='stockStatus')
    for stock in stocks:
        stock_elem = results.find('td', class_='stockStatus')
        if None in stock:
            continue
        if (stock_elem.text == 'In Stock'):
            print('IN STOCK AT B&H PHOTO\n')
    results = soup.find(id='tr50338')
    stocks = results.find_all('td', class_='stockStatus')
    for stock in stocks:
        stock_elem = results.find('td', class_='stockStatus')
        if None in stock:
            continue
        if (stock_elem.text != "Sold Out"):
            print('IN STOCK AT NEWEGG\n')
    URL = 'https://www.microcenter.com/search/search_results.aspx?Ntt=10600k&searchButton=search&storeid=191'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='productGrid')
    stocks = results.find_all('span',text='Sold Out')
    for stock in stocks:
        stock_elem = results.find('span',text='Sold Out')
        if None in stock:
            continue
        if (stock_elem.text !='Sold Out'):
            print('IN STOCK AT MICROCENTER\n')
    print("Done.\n\n")
schedule.every(5).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)

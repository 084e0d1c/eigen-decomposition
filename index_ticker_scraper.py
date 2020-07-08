import pandas as pd
from pandas_datareader import data as wb
from bs4 import BeautifulSoup
import requests

req_headers = {
                "Connection": "keep-alive",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0",
                "Accept-Language": "en"
              }

def get_index_ticker(index):
    exchange_dict = {
                    'r2000':'https://money.cnn.com/data/markets/russell/?page=1',
                    'spx':'https://money.cnn.com/quote/quote.html?symb=SPX&page=1',
                    'ndx':'https://money.cnn.com/quote/quote.html?symb=NDX&page=1',
                    'dji':'https://money.cnn.com/data/dow30/?page=1',
                    'djt':'https://money.cnn.com/data/markets/dowtrans/?page=1',
                    'dju':'https://money.cnn.com/quote/quote.html?symb=DJU&page=1',
                    'nya':'https://money.cnn.com/data/markets/nyse/?page=1'
                    }
    base_url = exchange_dict[index]
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text,features = 'html.parser')
    try:
        pages = soup.findAll('div',{'class':'paging'})[0].text.split()[-1]
    except:
        pages = 0
    tickers = []
    for page in range(int(pages)+1):
        url = base_url[:-1] + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text,features = 'html.parser')
        list_of_tickers = soup.findAll('a',{'class':'wsod_symbol'})
        for t in list_of_tickers:
            tickers.append(t.text)
    return tickers

def buildPriceDf(tickers,data_start_date,interval='1d'):
    df = pd.DataFrame()
    for i in tickers:
        try:
            df[i] = wb.DataReader(i,data_source='yahoo',start=data_start_date,end=datetime.today())['Adj Close']
            print('Successfully retrieved the price data for:',i)
        except:
            print('Failed to retrieve price data for: ',i)
            continue
    return df
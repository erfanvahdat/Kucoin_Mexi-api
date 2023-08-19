
import requests
import datetime
import pandas as pd

def kucoin(symbol,start,end,interval=None):
    
    start=datetime.datetime.timestamp(datetime.datetime.strptime(start,'%Y-%m-%d'))
    end=datetime.datetime.timestamp(datetime.datetime.strptime(end,'%Y-%m-%d'))

    # &startAt={int(start)}&startAt={int(end)}
    data=requests.get(f'https://api.kucoin.com/api/v1/market/candles?type=3min&symbol={symbol}-USDT&startAt={int(start)}').json()
    data=pd.DataFrame(data)['data']
    data=pd.DataFrame(list(data))
    data.columns=['time','Open','Close','High','Low','Volume','Closetime',]
    data.index=[datetime.datetime.fromtimestamp(int(i))   for i in data.loc[:,'time'] ]
    data=data.drop(['time'],axis=1)
    data=data.iloc[::-1]
    return data

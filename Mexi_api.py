
import requests
import datetime
import pandas as pd

def mexi(ticker,limit):

    # for ticker in Currency_list:
    #     ticker=ticker.upper()
    try:
        data=requests.get(f'https://api.mexc.com/api/v3/klines?symbol={ticker}USDT&interval=5m&limit={limit}').json()

        data=pd.DataFrame(data)
        data.iloc[:,0]=[datetime.datetime.fromtimestamp(float(i) / 1e3)   for i in data.iloc[:,0] ]
        data=pd.DataFrame(data)
        index =data.iloc[:,0]
        data.columns=['time','Open','High','Low','Close','Volume','Closetime','Quatasset']
        data.columns = map(str.capitalize, data.columns)
        data.index=data['Time']
        data=data.loc[:,['Open','High','Low','Close','Volume']]
        # Turn string data into float type
        data=data.astype('float')
        return data
    except:

        print(ticker+' does not exit')

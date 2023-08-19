

import datetime
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go
from pandas._libs.algos import backfill
from plotly.graph_objs.layout import grid

# mexi crypto api with 5 minutes interval
def mexi(ticker,limit):
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


# Kucoin crypto api with 3 minutes interval
# Type of candlestick patterns for kucoin_api: 1min, 3min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 8hour, 12hour, 1day, 1week
def kucoin(symbol,start,end,interval=None):
    try:
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
    except:
        print(ticker+' does not exit')


data=kucoin("BTC",'2023-08-18','2023-08-19')

fig = go.Figure()
fig.add_trace(go.Candlestick(x=data.index,open=data.Open,
                high=data.High,low=data.Low,
                close=data.Close,name='OHLC_data'
                ))
fig.update_layout(xaxis_rangeslider_visible=False,title='Data',xaxis_title='Date',
                yaxis_title='Price',plot_bgcolor='white',width=1600 ,height=600,showlegend=False,)
fig.show()

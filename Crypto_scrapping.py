import pandas as pd
import numpy as np
import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd
from datetime import datetime
today=datetime.today().strftime('%Y-%m-%d')

def get_history(name):
    yahoo_financials = YahooFinancials('{}-INR'.format(name))
    data=yahoo_financials.get_historical_price_data("2010-01-01", today, "daily")
    df = pd.DataFrame(data['{}-INR'.format(name)]['prices'])
    df = df.drop('date', axis=1)
    df.rename(columns = {'formatted_date':'date'}, inplace = True)
    df=df[['date','high','low','open','close','volume']]
    return df

def get_present_data(abvr):
    # define lists to hold the present data of different cryptos
    current_volume=[]
    market_cap=[]
    mov_avg_200=[]
    mov_avg_50=[]
    current_price=[]
    # iterating through the names and fetching the data
    for i in abvr:
        yahoo_financials = YahooFinancials('{}-INR'.format(i))
        vol=yahoo_financials.get_current_volume()
        cap=yahoo_financials.get_market_cap()
        ma_200=yahoo_financials.get_200day_moving_avg()
        ma_50=yahoo_financials.get_50day_moving_avg()
        cp=yahoo_financials.get_current_price()
        current_volume.append(vol)
        market_cap.append(cap)
        mov_avg_200.append(ma_200)
        mov_avg_50.append(ma_50)
        current_price.append(cp)

    # convert the data to dataframe
    df = pd.DataFrame(list(zip(abvr,current_price,current_volume,market_cap,mov_avg_200,mov_avg_50)),columns =['Abvr','current_price','current_volume','market_cap','MA_200','MA_50'])
    return df
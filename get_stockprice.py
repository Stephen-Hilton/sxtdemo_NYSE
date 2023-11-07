import yfinance as yf
import pandas as pd
import numpy as np
import os 
from pprint import pprint
from datetime import datetime
from spaceandtime import SpaceAndTime

def download_stock_prices(symbol, start_date, end_date):
    try:
        # Download Apple stock data
        data = yf.download(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print("Error occurred while fetching the data:", e)
        return None



if __name__ == "__main__":
    start_date = "2023-01-01"  # Replace with your desired start date
    end_date =  datetime.now().strftime('%Y-%m-%d')

    sxt = SpaceAndTime()
    sxt.authenticate()

    tamperproof = True
    tablename = 'SXTDemo.Stocks_Tamperproof' if tamperproof else 'SXTDemo.Stocks'
    biscuit = os.getenv('BISCUIT')

    sxt.execute_query(f'DELETE from {tablename}', biscuits=biscuit)

    for symbol in ['AAPL','MSFT','GOOGL', 'AMZN']:
        data = download_stock_prices(symbol, start_date, end_date)
        c = ' '
        if data is not None:
            data = pd.DataFrame(data).reset_index() # add date (from index)
            data.insert(loc=0, column='Symbol', value=symbol) # add symbol to front
            if tamperproof: data['PROOF_ORDER'] = np.arange(data.shape[0]) # add Proof_Order to end

            sql = [f"insert into {tablename} (Symbol, Stock_Date, Stock_Open, Stock_High, Stock_Low, Stock_Close, Stock_AdjClose, Stock_Volume{', Proof_Order' if tamperproof else ''}) values "]
            for idx, row in data.iterrows():
                if tamperproof:
                    sql.append(f"{c}('{row['Symbol']}', '{str(row['Date']).split(' ')[0]}', {round(row['Open'],2)}, {round(row['High'],2)}, {round(row['Low'],2)}, {round(row['Close'],2)}, {round(row['Adj Close'],2)}, {round(row['Volume'],2)}, {row['PROOF_ORDER']} )")
                else:
                    sql.append(f"{c}('{row['Symbol']}', '{str(row['Date']).split(' ')[0]}', {round(row['Open'],2)}, {round(row['High'],2)}, {round(row['Low'],2)}, {round(row['Close'],2)}, {round(row['Adj Close'],2)}, {round(row['Volume'],2)} )")
                c = ","
            sql = ''.join(sql)

            success, response = sxt.execute_query(sql_text=sql, sql_type=sxt.SQLTYPE.DML, resources='SXTDEMO.STOCKS', biscuits=biscuit)

            if success: 
                pprint(sxt.execute_query(f'Select * from {tablename}'))
            else:
                print(response)

        else:
            print("Failed to fetch stock prices.")

    print('\n\nDone!\n\n')
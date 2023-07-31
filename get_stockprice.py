import yfinance as yf
import pandas as pd
from datetime import datetime
import pySXT 

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
    sxt = pySXT.sxt('.env')
    success, access_token, refresh_token, reauth_datetime = sxt.authenticate()


    for symbol in ['AAPL','MSFT','GOOGL', 'AMZN']:
        data = download_stock_prices(symbol, start_date, end_date)
        c = ' '
        if data is not None:
            data = pd.DataFrame(data).reset_index() # add date (from index)
            data.insert(loc=0, column='Symbol', value=symbol) # add symbol

            sql = ["insert into SXTDEMO.STOCKS (Symbol, Stock_Date, Stock_Open, Stock_High, Stock_Low, Stock_Close, Stock_AdjClose, Stock_Volume) values "]
            for idx, row in data.iterrows():
                sql.append(f"{c}('{row['Symbol']}', '{str(row['Date']).split(' ')[0]}', {round(row['Open'],2)}, {round(row['High'],2)}, {round(row['Low'],2)}, {round(row['Close'],2)}, {round(row['Adj Close'],2)}, {round(row['Volume'],2)} )")
                c = ","
            sql = ''.join(sql)

            status_code, json_response = sxt.query_dml(resourceId='SXTDEMO.STOCKS', sql=sql)

            if status_code != 200: 
                print(json_response)

        else:
            print("Failed to fetch stock prices.")

    print('\n\nDone!\n\n')
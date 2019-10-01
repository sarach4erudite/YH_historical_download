import yfinance as yf
import pandas as pd 
import time 

quotes = ["^VIX", "^GSPC"]    # download quote can add more than one quote

start_date = '2008-01-01'
end_date =  '2018-11-13'      # make sure end_date > start_date and end_date <= today_date

# Download all stock quotes in the list     
for ticker in quotes :
    csv_name = "Data/daily_"+ticker+".csv" 

    #Download until success 
    while True : 
        try : 
            print("Start Downloading : " + ticker)
            data = yf.download(ticker, start=start_date, end=end_date)
            print("Download Completed")
            data.to_csv(csv_name)
            print("Saved : " + csv_name)
            break
        except KeyboardInterrupt:
            print("Cancel Download by user")
        except : 
            print("Download daily data from yahoo finance failed")
            print("Press Ctrl+C to cancel download")
            time.sleep(1)   # wait for request again


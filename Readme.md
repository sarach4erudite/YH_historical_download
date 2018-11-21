### Download historical data from Yahoo-finance to csv file with Python 3 

## Require libraries
1. pandas -> pip install pandas 
2. fix_yahoo_finance -> pip install fix-yahoo-finance   
   
   detail : https://pypi.org/project/fix-yahoo-finance/ 

## Choose tickers/quotes name 
change the quotes [list] in "download_from_yahoo.py", must be in the available quote(s) on Yahoo. 

## Change download date 
change start_date and end_date in format "YYYY-mm-dd", if there are no data during the date-range it will get error ! 

Example how to edit the file :
 
"download_from_yahoo.py" 
        
        line[5] : quotes = ["^VIX", "^GSPC"]    # for quote "VIX" and "GSPC"
        line[7] : start_date = '2008-01-01'
        line[8] : end_date =  '2018-11-13'      # make sure end_date > start_date and end_date <= today_date

  ### Running : 
                python download_from_yahoo.py

### After running the python file, the csv files are in the "Data" folder.


### Note : For Thailand Stock Exchange Data (SET) use "stockname.BK"

Example : 
         
         "CPALL.BK" for CPALL
         "PTT.BK"   for PTT 
         


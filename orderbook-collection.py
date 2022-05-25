import time
import datetime
import requests
import pandas as pd

while(1):
    

    book = {}
    response = requests.get ('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=5')
    book = response.json()

    data = book['data']

    #print (data)
    
    bids = (pd.DataFrame(data['bids'])).apply(pd.to_numeric,errors='ignore')
    bids.sort_values('price', ascending=False, inplace=True)
    bids = bids.reset_index(); del bids['index']
    bids['type'] = 0
    
    asks = (pd.DataFrame(data['asks'])).apply(pd.to_numeric,errors='ignore')
    asks.sort_values('price', ascending=True, inplace=True)
    asks['type'] = 1 

    #print (bids)
    #print (asks)

    df = pd.concat([bids,asks])
    timestamp = datetime.datetime.now()
    req_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    df['quantity'] = df['quantity'].round(decimals=4)
    df['timestamp'] = req_timestamp
    #print (df)


    df.to_csv(timestamp.strftime('%Y-%m-%d-bithumb-btc-orderbook.csv'), index=False, header=False, mode = 'a')
   
    
    #should_write_header = os.path.exists(fn)
    #if should_write_header == False:
        #df.to_csv(fn, index=False, header=True, mode = 'a')
    #else:
        #df.to_csv(fn, index=False, header=False, mode = 'a')

  
    
    time.sleep(4.9)




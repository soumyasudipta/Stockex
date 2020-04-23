import time
import requests
import json
import sys
import mongodb.mongodatabase as mdb 

def jprint():
    try:
        api_url_base = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MSFT&apikey=demo"
        headers = {'Content-Type': 'application/json'} 
        api_url = '{0}account'.format(api_url_base)

        response = requests.get(api_url, headers=headers)

        insert_data = []

        if response.status_code == 200:
            y = json.loads(response.content.decode('utf-8'))["Weekly Time Series"]
            for x in y:
                date_time = x
                pattern = '%Y-%m-%d'
                epoch = int(time.mktime(time.strptime(date_time, pattern)))

                data = {
                    '_id':'MSFT' + '-' + str(epoch),
                    'open':float(y[x]["1. open"]),
                    'high':float(y[x]["2. high"]),
                    'low':float(y[x]["3. low"]),
                    'close':float(y[x]["4. close"]),
                    'volume':float(y[x]["5. volume"]),
                    'timestamp':epoch
                }

                insert_data.append(data)

            mdb.insert(insert_data,'weekly')
            
        else:
            return None
    except Exception:
        print("Cannot connect to network")

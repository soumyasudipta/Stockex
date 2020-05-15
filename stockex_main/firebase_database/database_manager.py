# import pyrebase
#
# config = {
#   "apiKey" : "AIzaSyAx74C9R7qNyrrPC8LxoZgBDvSlPG8T-OY",
#   "authDomain" : "stockex-soumyasudipta.firebaseapp.com",
#   "databaseURL" : "https://stockex-soumyasudipta.firebaseio.com",
#   "projectId" : "stockex-soumyasudipta",
#   "storageBucket" : "stockex-soumyasudipta.appspot.com",
#   "messagingSenderId" : "240783026657",
#   "appId" : "1:240783026657:web:f556e81b37b6b97f4f4aa0",
#   "measurementId" : "G-TR21G3F9RN"
# }
#
# firebase = pyrebase.initialize_app(config)
#
# auth = firebase.auth()
#
# db = firebase.database()
#
# data = {
#     "name": "Soumya Sudipta Sarangi"
# }
#
# import requests
# r = requests.get('https://finnhub.io/api/v1/forex/rates?token=bqit20frh5r89luqqa4g')
#
# print(r.json())
#
# results = db.child("forex").set(r.json()['quote'])
#
# print(results)

import requests

response = requests.get('https://api.tradier.com/v1/markets/history',
    params={'symbol': 'AAPL', 'interval': 'daily', 'start': '2019-05-04', 'end': '2019-05-04'},
    headers={'Authorization': 'Bearer XFfN46tKs0ij1AxYwCAYafdMbkUa', 'Accept': 'application/json'}
)
json_response = response.json()
print(response.status_code)
print(json_response)
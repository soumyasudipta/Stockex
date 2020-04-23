from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.test


def insert(data,database_name):
    try:
        if(database_name == 'monthly'):
            db.monthly.insert_many(data)
        if(database_name == 'weekly'):
            db.weekly.insert_many(data)
        if(database_name == 'daily'):
            db.daily.insert_many(data)
    except Exception:
        print(Exception)


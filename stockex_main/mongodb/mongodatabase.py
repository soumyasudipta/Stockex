from pymongo import MongoClient
client = MongoClient('mongodb+srv://stockex-mainserver:Soumya%401902@stockexcluster-1m7qb.gcp.mongodb.net/test?retryWrites=true&w=majority')
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


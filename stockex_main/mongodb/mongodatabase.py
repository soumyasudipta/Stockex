import logging

from pymongo import MongoClient
from mongodb.constants import connection_string

client = MongoClient(connection_string)

def insert(data,database_name,collection_name):
    try:
        client[database_name][collection_name].insert_many(data)
    except Exception:
        print(Exception)
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(Exception)


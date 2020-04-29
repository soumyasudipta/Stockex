import logging

import pymongo
from pymongo import MongoClient
from pymongo import errors
import mongodb.connection as connection

def insert(data, database_name, collection_name):
    try:
        client = connection.establish_connection()
        client[database_name][collection_name].insert_many(data)
        connection.end_connection(client)

    except errors.WriteError as e:
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)

def drop_collection(database_name, collection_name):
    try:
        client = connection.establish_connection()
        client[database_name][collection_name].drop()
        connection.end_connection(client)

    except errors.WriteError as e:
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
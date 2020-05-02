from pymongo import errors
from logger import logging_manager
import mongodb.connection as connection


def write_to_database(data, database_name, collection_name):
    try:
        client = connection.establish_connection()
        client[database_name][collection_name].insert_many(data,
                                                           ordered=False,
                                                           session=None)
        connection.end_connection(client)

    except errors.WriteError as e:
        logging_manager.logging_do(e, 40)


def drop_collection(database_name, collection_name):
    try:
        client = connection.establish_connection()
        client[database_name][collection_name].drop()
        connection.end_connection(client)

    except errors.WriteError as e:
        logging_manager.logging_do(e, 40)


def read_from_database(symbol, database_name, collection_name):
    try:

        cursor = 0
        client = connection.establish_connection()

        if collection_name in client[database_name].list_collection_names():
            cursor = list(client[database_name][collection_name] \
                .find({'_id': {'$regex': str(symbol)}}, {'timestamp': 1}) \
                .sort('timestamp', -1) \
                .limit(1))[0]['timestamp']

        connection.end_connection(client)

        return cursor

    except errors.WriteError as e:
        logging_manager.logging_do(e, 40)

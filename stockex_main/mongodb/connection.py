# Import global libraries
from logger import logging_manager
from pymongo import MongoClient
from pymongo import errors

# Import local libraries
from mongodb.constants import connection_string


# Function to connect to mongodb server
def establish_connection():
    try:
        client = MongoClient(connection_string)
        return client

    except errors.WriteError as e:
        logging_manager.logging_do(e, 40)


def end_connection(client):
    try:
        client.close()

    except errors.WriteError as e:
        logging_manager.logging_do(e, 40)

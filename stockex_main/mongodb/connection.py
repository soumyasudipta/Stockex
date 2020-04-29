# Import global libraries
import logging
from pymongo import MongoClient
from pymongo import errors

# Import local libraries
from mongodb.constants import connection_string

# Function to connect to mongodb server
def establish_connection():
    try:
        client = MongoClient(connection_string)
        print('Connection Opened')
        return client
    
    except errors.WriteError as e:
        logging.basicConfig(filename='app.log', 
                            filemode='w', 
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)


def end_connection(client):
    try:
        client.close()
        print('Connection Closed')
    
    except errors.WriteError as e:
        logging.basicConfig(filename='app.log', 
                            filemode='w', 
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
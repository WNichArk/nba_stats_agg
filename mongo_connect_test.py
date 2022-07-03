from pymongo import MongoClient
import constants.constants as cs

class database():

    def get_database(self, db_name):
        import pymongo
        from pymongo import MongoClient

        
        print("connection")
        client = MongoClient(cs.CONNECTION_STRING)

        return client[db_name]

    def __init__(self):
        pass
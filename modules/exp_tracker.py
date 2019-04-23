"""
Module to track experiments

We start with `MongoDB <https://api.mongodb.com/python/current/tutorial.html>`_.
"""
import pymongo
from pymongo import MongoClient


def connect_to_db(dbname, hostname='localhost', port=27017):
    """
    :param dbname: database name
    :type dbname: str
    :param hostname: hostname
    :type dbname: str
    :param port: connection port
    :type dbname: int
    :return: a connection to a database
    :rtype: pymongo.database.Database
    """
    client = MongoClient(hostname, port)
    return client[dbname]


if __name__ == '__main__':
    db_name = 'test_database'
    col_name = 'dicts'
    db = connect_to_db(db_name)
    print(isinstance(db, pymongo.database.Database))
    collection = db[col_name]
    collection.insert_one({'k1': 1, 'k2': 'a string'})
    print(col_name in db.list_collection_names())
    print(db.dicts.find_one({'k1': 1}))
    print(db.dicts.find_one({'k1': -999}) is None)
    print(collection.find_one_and_delete({'k1': 1}))
    print(db.dicts.find_one({'k1': 1}))
    print(collection.count_documents({'k1': 1}))
    collection.drop()
    print(col_name in db.list_collection_names())

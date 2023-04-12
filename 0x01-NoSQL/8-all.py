#!/usr/bin/env python3

"""
Module contains list_all function
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """

    return mongo_collection.find()

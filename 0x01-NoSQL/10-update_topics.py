#!/usr/bin/env python3


"""
this module contains the function update_topics
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """

    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}}).modified_count

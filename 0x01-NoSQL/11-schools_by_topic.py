#!/usr/bin/env python3

"""
Module contains the schools_by_topic
"""

from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Returns list of school having a specific topic
    """

    return mongo_collection.find({"topics": topic})

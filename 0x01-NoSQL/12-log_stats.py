#!/usr/bin/env python3


"""
This script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def logStats():
    ''' function that provides some stats about Nginx logs stored in MongoDB'''
    client = MongoClient()
    db = client["logs"]
    collection = db["nginx"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print(f"\tmethod {method}: " +
              f"{collection.count_documents({'method': method})}")

    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} \
status check")


if __name__ == "__main__":
    logStats()

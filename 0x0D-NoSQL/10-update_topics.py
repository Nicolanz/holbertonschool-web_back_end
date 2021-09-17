#!/usr/bin/env python3
"""Module to update a document of a mongo db collection"""


def update_topics(mongo_collection, name, topics):
    """Function to update many"""
    mongo_collection.update_many({'name': name}, {"$set": {"topics": topics}})

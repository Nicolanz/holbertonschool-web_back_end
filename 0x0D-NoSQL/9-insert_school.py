#!/usr/bin/env python3
"""Module to list all documents in python"""


def insert_school(mongo_collection, **kwargs):
    """Insert school function"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

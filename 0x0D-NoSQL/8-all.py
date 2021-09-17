#!/usr/bin/env python3
"""Module to list all documents in python"""


def list_all(mongo_collection):
    """Function to list the documents of a collection"""
    my_list = []
    elements = mongo_collection.find({})
    for i in elements:
        my_list.append(i)
    return my_list

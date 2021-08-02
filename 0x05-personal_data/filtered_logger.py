#!/usr/bin/env python3
"""Filter module"""
import re


def filter_datum(fields, redaction, message, separator):
    """Filter funtion"""
    new_str = re.sub(fields[0] + '=[a-z]*' + separator, fields[0] + "=" +
                         redaction + separator, message)
    new_str = re.sub(fields[1] + '=' + '.*' + separator, fields[1] +
                     "=" + redaction + separator, new_str)
    return new_str

#!/usr/bin/env python3
"""Filter module"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """Filter funtion"""
    new_str = re.sub(fields[0] + '=[a-z]*' + separator, fields[0] + "=" +
                     redaction + separator, message)
    new_str = re.sub(fields[1] + '=' + '.*' + separator, fields[1] +
                     "=" + redaction + separator, new_str)
    return new_str

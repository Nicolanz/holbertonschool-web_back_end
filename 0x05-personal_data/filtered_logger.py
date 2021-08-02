#!/usr/bin/env python3
"""Filter module"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """Filter function"""
    for i in fields:
        message = re.sub(i + '(=[a-z]*|=.*)' + separator, i + "=" +
                         redaction + separator, message)
    return message

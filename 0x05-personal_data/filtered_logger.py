#!/usr/bin/env python3
"""Filter module"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord):
        """Format method"""
        logging.basicConfig(level=record.levelname,
                            format=RedactingFormatter.FORMAT)
        logging.info(filter_datum(self.fields, self.REDACTION,
                     record.msg, self.SEPARATOR))


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """Filter function"""
    for i in fields:
        message = re.sub(r"(?<={}=)[^{}]*(?={})".format(i, separator,
                                                        separator),
                         redaction, message)
    return message

#!/usr/bin/env python3
"""Filter module"""
import re
from typing import List
import logging


PII_FIELDS: tuple = ("name", "email", "phone", "last_login", "password")


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

    def format(self, record: logging.LogRecord) -> str:
        """Format method"""
        msg = filter_datum(self.fields, self.REDACTION,
                           super().format(record), self.SEPARATOR)
        return msg


def filter_datum(fields: List[str],
                 redaction: str, message: str,
                 separator: str) -> str:
    """Filter function"""
    for i in fields:
        message = re.sub(r"(?<={}=)[^{}]*(?={})".format(i, separator,
                                                        separator),
                         redaction, message)
    return message


def get_logger() -> logging.Logger:
    """Get logger function"""
    user_data = logging.getLogger(name="user")
    user_data.addHandler(RedactingFormatter)
    return user_data

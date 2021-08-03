#!/usr/bin/env python3
"""Filter module"""
import re
from typing import List
import logging
import csv


PII_FIELDS = ("esto", "esto", "esto", "esto", "esto")


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


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
    """Get logger"""
    return logging.getLogger("user_data")

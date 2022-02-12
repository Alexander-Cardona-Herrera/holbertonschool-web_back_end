#!/usr/bin/env python3
"""
    Regex-ing
"""

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: [str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ message format """
        return filter_datum(self.fields, self.REDACTION, super().format(
            record), self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """ return a obfuscated message """

    for item in fields:
        message = re.sub("{}=.+?{}".format(item, separator), "{}={}{}".format(
            item, redaction, separator), message)
    return message

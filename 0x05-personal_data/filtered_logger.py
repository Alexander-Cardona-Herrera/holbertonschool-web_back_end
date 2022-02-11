#!/usr/bin/env python3
"""
0. Regex-ing
"""

from typing import List
import re


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """ return a obfuscated message """

    for item in fields:
        message = re.sub("{}=.+?{}".format(item, separator), "{}={}{}".format(
            item, redaction, separator), message)
    return message

# -*- coding: utf-8 -*-

"""Main module."""
import sys
import os
import json
try:
    import secrets
except ImportError as e:
    import random


def write_quote(language, json_decode):
    # Sort quotes by language
    sorted_quotes = [x for x in json_decode["quotes"] if x["lang"].lower() in language or "both" in language]

    # Get quote with imported module
    if "secrets" in sys.modules:
        to_print = secrets.choice(sorted_quotes)
    elif "random" in sys.modules:
        to_print = random.choice(sorted_quotes)

    # If not author is specified, the author will be chosen correspondingly to the language
    if not to_print["author"]:
        if len(language) == 1 or (len(language) > 1 and "en" not in language):
            author = json_decode["langs"][language[0].upper()]
        else:
            author = "Unknown"
    else:
        author = to_print["author"]

    # Print the actual quote
    print(to_print["quote"])
    print("-" + author)

# -*- coding: utf-8 -*-

"""Main module."""
import sys
import json
try:
    import secrets
except ImportError as e:
    import random


def write_quote():
    to_print = get_quote()

    print(to_print["quote"])
    print("-" + to_print["author"])


def get_quote():
    json_decode = []
    with open("quotes.json") as json_file:
        json_decode = json.load(json_file)

    if "secrets" in sys.modules:
        to_print = secrets.choice(json_decode)
    elif "random" in sys.modules:
        to_print = random.choice(json_decode)

    return to_print

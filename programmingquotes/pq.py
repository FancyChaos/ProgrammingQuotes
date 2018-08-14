# -*- coding: utf-8 -*-

"""Main module."""
import sys
import os
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
    path = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(path, "quotes.json")

    json_decode = []
    with open(json_path) as json_file:
        json_decode = json.load(json_file)

    if "secrets" in sys.modules:
        to_print = secrets.choice(json_decode)
    elif "random" in sys.modules:
        to_print = random.choice(json_decode)

    return to_print

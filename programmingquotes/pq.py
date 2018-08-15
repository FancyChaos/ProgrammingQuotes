# -*- coding: utf-8 -*-

"""Main module."""
import sys
import os
import json
try:
    import secrets
except ImportError as e:
    import random



def write_quote(lang):
    # Get path of quotes.json
    path = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(path, "quotes.json")

    # Open quotes.json
    json_decode = []
    with open(json_path) as json_file:
        json_decode = json.load(json_file)
    
    # Sort quotes by language
    sorted_quotes = [x for x in json_decode if x["lang"].lower() == lang.lower() or lang == "both"]
   
    # Get quote with imported module
    if "secrets" in sys.modules:
        to_print = secrets.choice(sorted_quotes)
    elif "random" in sys.modules:
        to_print = random.choice(sorted_quotes)
    
    # If not author is specified, the author will be chosen correspondingly to the language
    if not to_print["author"]:
        author = "Unbekannt" if lang.lower() == "de" else "Unknown"
    else:
        author = to_print["author"]
    
    # Print the actual quote
    print(to_print["quote"])
    print("-" + author)

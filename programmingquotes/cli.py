# -*- coding: utf-8 -*-

"""Console script for programmingquotes."""
import sys
import click
import json
import os
from . import pq


@click.command()
@click.option("--language", "-l", default="both", help="Pick your language (DE/EN). Ignore it for all languages")
@click.option("--quotes", "-q", is_flag=True, help="List number of quotes")
def main(language, quotes):
    # language to lower
    language = [x.lower() for x in language.split()]
    
    # Get path of quotes.json
    path = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(path, "quotes.json")

    # Open quotes.json 
    json_decode = []
    with open(json_path) as json_file:
        json_decode = json.load(json_file)
    
    # Get every supported language
    valid_langs = [x.lower() for x in json_decode["langs"].keys()]
    
    # -q and -l cant be enabled at the same time
    if quotes and "both" not in language:
        print("[!] Invalid arrangement of arguements")
        return 0
    # If the language is not supported yet
    elif any(x not in valid_langs for x in language):
        print("[!] specified language not supported yet")
        return 0

    # If quotes option is defined
    if quotes:
        # Get amount of quotes in every language
        quotes_by_lang = {}
        for lang in valid_langs:
            if lang != "both":
                quotes_by_lang[lang] = str(len([x for x in json_decode["quotes"] if x["lang"].lower() == lang]))
        quotes_by_lang["total"] = str(len(json_decode["quotes"]))
        
        # Print them out
        for k, v in quotes_by_lang.items():
            print(k + ": " + v + " quotes avaiable")

        return 0
    
    pq.write_quote(language, json_decode)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

# -*- coding: utf-8 -*-

"""Main module."""
import json
import secrets


def main():
    json_decode = []
    with open("quotes.json") as json_file:
        json_decode = json.load(json_file)
    to_print = secrets.choice(json_decode)
    print(to_print["quote"])
    print("-" + to_print["author"])


if __name__ == "__main__":
    main()

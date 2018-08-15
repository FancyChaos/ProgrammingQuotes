# -*- coding: utf-8 -*-

"""Console script for programmingquotes."""
import sys
import click
from . import pq


@click.command()
@click.option("--language", "-l", default="both", help="Pick your language (DE/EN). Leave it empty for all languages")
def main(language):
    valid_langs = ["DE", "EN", "both"]
    if any(x.lower() in language.lower() for x in valid_langs):
        pq.write_quote(language)
    else:
        print("[!] specified language not supported")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

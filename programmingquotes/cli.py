# -*- coding: utf-8 -*-

"""Console script for programmingquotes."""
import sys
import click
from . import programmingquotes as pq


@click.command()
def main(args=None):
    """Console script for programmingquotes."""
    pq.write_quote()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

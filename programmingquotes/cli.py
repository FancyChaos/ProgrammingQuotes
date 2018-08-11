# -*- coding: utf-8 -*-

"""Console script for programmingquotes."""
import sys
import click
import programmingquotes


@click.command()
def main(args=None):
    """Console script for programmingquotes."""
    programmingquotes.write_quote()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

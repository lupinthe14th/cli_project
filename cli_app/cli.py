#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CLI arguments definition.


"""
from argparse import ArgumentParser
from argparse import OPTIONAL

from . import __version__

parser = ArgumentParser(
    prog="cli",
    description="This is cli application.")

#######################################################################
# Positional arguments.
#######################################################################

positional = parser.add_argument_group(
    title='Positional Arguments',
    description="""
    These arguments come after any flags and in the order they are listed here.
    from address, to address and dete is required.
    option time.
    """
)

positional.add_argument(
    'fromaddr',
    metavar='FROMADDR',
    help="""Envelove from address."""
)

positional.add_argument(
    'toaddr',
    metavar='TOADDR',
    help="""Envelove to address."""
)

positional.add_argument(
    'date',
    metavar='DATE',
    help="""date formats ISO8601."""
)

positional.add_argument(
    'time',
    metavar='TIME',
    nargs=OPTIONAL,
    help="""time formats  ISO8601."""
)

#######################################################################
# Troubleshooting
#######################################################################

troubleshooting = parser.add_argument_group(title='Troubleshooting')

troubleshooting.add_argument(
    '--version',
    action='version',
    version=__version__,
    help="""
    Show version and exit.
    """
)

troubleshooting.add_argument(
    '--debug',
    action='store_true',
    default=False,
    help="""
    Prints the exception traceback should one occur, as well as other
    information useful for debugging cli itself and for reporting bugs.
    """
)

# vim fileencoding=utf-8

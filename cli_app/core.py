#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides the main functionality of HTTPie.

Invocation flow:

  1. Read, validate and process the input (args, `stdin`).
  2. Create and execute a command.
  3. Write to `stdout`
  4. Exit.

"""

import sys

from logging import getLogger
from logging import basicConfig
from logging import DEBUG
from logging import INFO

from . import ExitStatus
from .validations import PositionalArgs

logger = getLogger(__name__)

def program(args):
    """
    The main program without error handling
    
    :param args: parsed args (argparse.Namespace)
    :return: status code
    
    """
    exit_status = ExitStatus.OK

    logger.debug('args: {}'.format(args))
    logger.debug('args.fromaddr: {}'.format(args.fromaddr))
    logger.debug('args.toaddr: {}'.format(args.toaddr))
    logger.debug('args.date: {}'.format(args.date))
    logger.debug('args.time: {}'.format(args.time))

    pa = PositionalArgs()
    pa.fromaddr = args.fromaddr
    pa.toaddr = args.toaddr
    pa.date = args.date
    pa.time = args.time

    try:
        pa.validate()
    except:
        exit_status = ExitStatus.ERROR
        raise

    return exit_status

def main(args=sys.argv[1:]):
    """
    The main function.

    Pre-process args, handle some special types of invocations,
    and run the main program with error handling.
    Return exit status code.
    
    """
    
    from cli_app.cli import parser
    try:
        parsed_args = parser.parse_args(args=args)
    except SystemExit as e:
        exit_status = ExitStatus.ERROR
    else:
        if parsed_args.debug:
            basicConfig(level=DEBUG)
        else:
            basicConfig(level=INFO)
        logger.debug("{}".format(parsed_args))

        try:
            exit_status = program(args=parsed_args)
        except KeyboardInterrupt:
            exit_status = ExitStatus.ERROR_CTRL_C
        except Exception as e:
            error_type = type(e).__name__
            logger.error("{0}: {1}".format(error_type, e.messages))
            exit_status = ExitStatus.ERROR

    logger.debug('exit_status: {}'.format(exit_status))
    return exit_status

# vim fileencoding=utf-8

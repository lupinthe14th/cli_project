#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cli application template.

"""
__version__ = '1.0.0-dev'
__author__ = 'Hideo Suzuki'
__licence__ = 'MIT'


class ExitStatus:
    """Exit status code constants."""

    OK = 0
    ERROR = 1

    # 128+2 SIGINT <http://www.tldp.org/LDP/abs/html/exitcodes.html>
    ERROR_CTRL_C = 130

# vim fileencoding=utf-8

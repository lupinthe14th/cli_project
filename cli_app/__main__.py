#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The main entry point. Invoke as `cli' or `python -m cli_app'.

"""

import sys

def main():
    try:
        from .core import main
        sys.exit(main())
    except KeyboardInterrupt:
        from . import ExitStatus
        sys.exit(ExitStatus.ERROR_CTRL_C)

if __name__ == '__main__':
    main()

# vim fileencoding=utf-8

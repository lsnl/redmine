#!/usr/bin/env python3

import os
import sys
import argparse
import unicodedata

from redminelib import Redmine
from redmine import Handler


def main():
    handler = Handler()

    if hasattr(handler.args, 'handler'):
        handler.args.handler(handler.args)
    else:
        handler.parser.print_help()


if __name__ == '__main__':
    main()

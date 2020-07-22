#!/usr/bin/env python3

import os
import sys
import argparse
import unicodedata

from redminelib import Redmine
from lib import Projects, Issues, Handler


def main():
    handler = Handler()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

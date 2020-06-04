#!/usr/bin/env python3

import os
import sys
import argparse

from redminelib import Redmine

SERVER_URL = 'http://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')


def fetch_projects(redmine, query=None):
    # TODO: separate processing by query

    return redmine.project.all()


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('commands', nargs='+')
    args = parser.parse_args()
    commands = vars(args)['commands']

    if len(commands) < 1:
        parser.print_help()

    if API_ACCESS_KEY is None:
        print('please set REDMINE_API_ACCESS_KEY')
        sys.exit(1)

    redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

    if commands[0] == 'projects':
        query = None
        if len(commands) >= 2:
            query = commands[1]
        projects = fetch_projects(redmine, query)
        print('\n'.join(map(str, projects)))


if __name__ == '__main__':
    main()

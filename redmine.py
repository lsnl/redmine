#!/usr/bin/env python3

import os
import sys
import argparse
import unicodedata

from redminelib import Redmine

SERVER_URL = 'http://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('commands', nargs='+')
    args = parser.parse_args()
    return args


def fetch_projects(redmine):
    return redmine.project.all()


def fetch_issue(redmine, resource_id=None):
    if resource_id is None:
        sys.exit(1)
    return redmine.issue.get(resource_id)


def fetch_issues(redmine):
    return redmine.issue.all()


def print_issues(issues):
    def japanese_limit(word, limit):
        result = ''
        for c in word:
            if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
                limit -= 2
            else:
                limit -= 1
            result += c

            if limit == 0:
                return result
            elif limit == 1:
                return result + ' '

        return word + ' '*limit

    keys_with_size = [('id', 4), ('project', 24), ('status', 8),
                      ('priority', 8), ('subject', 32), ('assigned_to', 16)]
    for key, sz in keys_with_size:
        print(japanese_limit(key, sz), end=' ')
    print()

    sorted_issues = sorted(issues, key=lambda x: x['id'])

    for issue in sorted_issues:
        own_keys = [iss[0] for iss in issue]
        for key, sz in keys_with_size:
            if key in own_keys:
                print(japanese_limit(str(issue[key]), sz), end=' ')
            else:
                print(' '*sz, end=' ')
        print()


def main():
    args = parse_args()
    commands = args.commands

    if len(commands) < 1:
        parser.print_help()

    if API_ACCESS_KEY is None:
        print('please set REDMINE_API_ACCESS_KEY')
        sys.exit(1)

    redmine = Redmine(SERVER_URL, key=API_ACCESS_KEY)

    if commands[0] == 'projects':
        if len(commands) < 2 or commands[1] != 'list':
            # TODO: display help
            sys.exit(1)
        projects = fetch_projects(redmine)
        print('\n'.join(map(str, projects)))

    elif commands[0] == 'issues':
        if len(commands) < 2:
            # TODO: display help
            sys.exit(1)
        if commands[1] == 'list':
            issue = fetch_issues(redmine)
            print_issues(issue)
        elif commands[1] == 'view':
            pass
        elif commands[1] == 'create':
            pass
        elif commands[1] == 'update':
            pass
        elif commands[1] == 'delete':
            pass
        else:
            # TODO: display help
            sys.exit(1)


if __name__ == '__main__':
    main()

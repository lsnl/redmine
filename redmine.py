#!/usr/bin/env python3

import os
import sys
import argparse
import unicodedata

from redminelib import Redmine

SERVER_URL = os.getenv('REDMINE_SERVER_URL')
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('commands', nargs='+')
    args = parser.parse_args()
    return parser, args


def fetch_projects(redmine):
    return redmine.project.all()


def fetch_issue(redmine, resource_id=None):
    if resource_id is None:
        sys.exit(1)
    return redmine.issue.get(resource_id, status_id='*')


def fetch_issues(redmine):
    return redmine.issue.all(sort='id')


def print_issue(issue):
    keys = [('id', '#'), ('subject', 'Subject'), ('status', 'Status'),
            ('priority', 'Priority'), ('assigned_to', 'Assignee'),
            ('start_date', 'Start date'), ('due_date', 'Due date'),
            ('done_ratio', '% Done'), ('estimated_hours', 'Estimated time')]

    for key, name in keys:
        print('{:16}{}'.format(name, getattr(issue, key, '')))
    print('Description')
    print(issue['description'], end='\n\n')
    print('Subtasks')
    print_resource_set(issue['children'])
    print('Related issues')
    print(getattr(issue, 'relation', ''))


def print_issues(issues):
    def japanese_limit(word, limit):
        result = ''
        for c in word:
            limit -= 1
            if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
                limit -= 1
            result += c
            if limit <= 1:
                return result + ' ' * limit
        return word + ' ' * limit

    keys_with_size = [('id', 4), ('project', 24), ('status', 8),
                      ('priority', 10), ('subject', 32), ('assigned_to', 16)]
    for key, sz in keys_with_size:
        print(japanese_limit(key, sz), end=' ')
    print()

    for issue in issues:
        for key, sz in keys_with_size:
            line_value = getattr(issue, key, '')
            print(japanese_limit(str(line_value), sz), end=' ')
        print()


def print_resource_set(resource_set):
    if len(resource_set) > 0:
        print_issues(resource_set)
    print()


def main():
    parser, args = parse_args()
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
            if len(commands) < 3:
                sys.exit(1)
            issue = fetch_issue(redmine, commands[2])
            print_issue(issue)
        else:
            # TODO: display help
            sys.exit(1)


if __name__ == '__main__':
    main()

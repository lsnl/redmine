#!/usr/bin/env python3

import os
import sys
import argparse
import unicodedata

from redminelib import Redmine
from redminelib.exceptions import ResourceAttrError

SERVER_URL = 'https://rm.lsnl.jp/'
API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')

assigned2id = {
    "ohsaki": 5,
    "akio": 7,
    "chuta": 8,
    "kei": 9,
    "keita": 10,
    "ryota": 11,
    "ryotaro": 12,
    "taisei": 13,
    "joe": 14,
    "ryuichiro": 15,
    "yuhei": 16,
    "takeaki": 17,
    "yuki": 18,
    "michika": 19,
    "kaz": 20,
    "soma": 21,
    "kohei": 22,
    "hal": 23,
    "eriko": 24,
    "han": 27,
    "ko": 28,
    "nanami": 29,
    "shota": 30,
    "yukihiro": 31,
    "takeki": 32,
    "empty": '!*'
}

project2id  = {
    'thema': 1,
    'bootcamp': 2,
    'admin': 3,
    'goods': 4,
    'event': 5,
    'unix-bof': 6,
    'math-bof': 7,
    'training': 8,
    'ryota': 9,
    'ryotaro': 10,
    'keita': 11,
    'joe': 12,
    'michika': 13,
    'chuta': 14,
    'kaz': 15,
    'ryuichiro': 16,
    'soma': 17,
    'yuhei': 19,
    'akio': 20,
    'kei': 21,
    'yuki': 22,
    'taisei': 23,
    'takeaki': 24,
    'seminar': 25,
    'travel': 26,
    'meeting': 27,
    'kohei': 28,
    'student-meeting': 29,
    'workshop': 30,
    'ict': 31
}

def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('commands', nargs='+')
    parser.add_argument('-p', help='Project name')
    parser.add_argument('-a', help='Assigned_to name')
    parser.add_argument('-s', help='Status name')
    args = parser.parse_args()
    return args

def fetch_projects(redmine):
    return redmine.project.all()

def fetch_issues(redmine):
    return redmine.issue.all(sort='id')

def fetch_issues_in_project(redmine, name, status):
    return redmine.issue.filter(project_id=project2id[name], status_id=status)

def fetch_assigned_issues(redmine, name, status):
    if name == 'empty':
        return redmine.issue.filter(assigned_to_id=assigned2id[name],status_id=status,tracker_id='5')
    else:
        return redmine.issue.filter(assigned_to_id=assigned2id[name],status_id=status)

def fetch_issue(redmine, resource_id=None):
    if resource_id is None:
        sys.exit(1)
    return redmine.issue.get(resource_id, status_id='*')
    
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
                      ('priority', 10), ('subject', 32), ('assigned_to', 16), ('due_date', 11)]
    for key, sz in keys_with_size:
        print(japanese_limit(key, sz), end=' ')
    print()

    for issue in issues:
        for key, sz in keys_with_size:
            line_value = getattr(issue, key, '')
            print(japanese_limit(str(line_value), sz), end=' ')
        print()
        
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
    for journal in issue.journals:
        try:
            print(journal.notes)
            print()
        except ResourceAttrError:
            pass
        
def print_resource_set(resource_set):
    if len(resource_set) > 0:
        print_issues(resource_set)

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
        if commands[1] == 'list':
            status = str(args.s) if args.s else 'open'
            if args.p:
                issue = fetch_issues_in_project(redmine, args.p, status)
            elif args.a:
                issue = fetch_assigned_issues(redmine, args.a, status)
            else:
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

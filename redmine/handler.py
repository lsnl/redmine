import sys
import os
from redminelib import Redmine
from redmine.projects import Projects
from redmine.issues import Issues
import argparse


class Handler():
    def __init__(self):
        self.SERVER_URL = 'https://rm.lsnl.jp/'
        self.API_ACCESS_KEY = os.getenv('REDMINE_API_ACCESS_KEY')
        self.check_env()
        self.parser, self.args = self.parse_args()
        self.redmine = Redmine(self.SERVER_URL, key=self.API_ACCESS_KEY)

    def parse_args(self):
        parser = {}
        parser["top"] = argparse.ArgumentParser(description='')
        subparsers = parser["top"].add_subparsers()

        parser["projects"] = subparsers.add_parser("projects")
        parser["projects"].add_argument("list")
        parser["projects"].set_defaults(handler=self.handle_projects)

        parser["issues"] = subparsers.add_parser("issues")
        parser["issues"].add_argument("list")
        parser["issues"].set_defaults(handler=self.handle_issues)

        args = parser["top"].parse_args()
        return parser, args

    def check_env(self):
        if not self.SERVER_URL:
            print("please set SERVER_URL")
            sys.exit(1)
        if not self.API_ACCESS_KEY:
            print("please set API_ACCESS_KEY")
            sys.exit(1)

    def handle_projects(self, command):
        projects = Projects(self.redmine)
        if hasattr(command, 'list'):
            print(projects.list_projects())

    def handle_issues(self, command):
        issues = Issues(self.redmine)
        if hasattr(command, 'list'):
            print(issues.print_issues())

class Projects():
    def __init__(self, redmine):
        self.projects = self.fetch_projects(redmine)

    def fetch_projects(self, redmine):
        return redmine.project.all()

    def list_projects(self):
        print('\n'.join(map(str, self.projects)))

import unicodedata


class Issues():
    def __init__(self, redmine):
        self.issues = self.fetch_issues(redmine)

    def fetch_issues(self, redmine):
        return redmine.issue.all(sort='id')

    def print_issues(self):
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
                          ('priority', 10), ('subject', 32),
                          ('assigned_to', 16)]
        for key, sz in keys_with_size:
            print(japanese_limit(key, sz), end=' ')
        print()

        for issue in self.issues:
            for key, sz in keys_with_size:
                line_value = getattr(issue, key, '')
                print(japanese_limit(str(line_value), sz), end=' ')
            print()

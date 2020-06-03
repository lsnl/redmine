# redmine

## Installation

clone project

```zsh
git clone https://github.com/lsnl/redmine.git
cd redmine
```

install requre modules

```zsh
pip install -r requirements.txt
```

set REDMINE_API_ACCESS_KEY to your environment variable

> You can see your API access key in http://rm.lsnl.jp/my/account

```zsh
export REDMINE_API_ACCESS_KEY="XXX"
```

## Usage

### projects

fetch projects

```zsh
./redmine.py projects
```

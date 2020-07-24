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

set `REDMINE_SERVER_URL` and `REDMINE_API_ACCESS_KEY` to your environment variable

> You can see your API access key in https://rm.lsnl.jp/my/account

```zsh
export REDMINE_SERVER_URL="https://rm.lsnl.jp/"
export REDMINE_API_ACCESS_KEY="XXX"
```

## Usage

### projects

show projects list

```zsh
redmine projects list
```

result example

```
勉強会:UNIXを楽しむ会
勉強会:ブートキャンプ
勉強会:数学を楽しむ会
勉強会:自主勉強会
勉強会:輪講
```

### show

```zsh
redmine show -p seminar
```

### issues

issues

```zsh
redmine issues [list, view, create, update, delete]
```

#### list

##### filter with project name

```zsh
redmine issues list -p $project_name (-s $status)
```

result example

```
id Project       Status Priority        Subject          Assignee   due_date
1 研究:テーマ考案 ToDo   通常     2020-06-05 12:40-13:30   Alice     2020-07-09
2 研究:テーマ考案 ToDo   通常     2020-06-07 12:40-13:30   Bob       2020-07-16
```

##### filter with assignee name

```zsh
redmine issues list -a $assignee_name (-s $status)
```

result example

```
id Project             Status Priority        Subject          Assignee   due_date
1 勉強会:UNIXを楽しむ会   ToDo   通常     2020-06-05 12:40-13:30   Alice     2020-06-05
2 勉強会:数学を楽しむ会    ToDo   通常     2020-06-09 12:40-13:30   Alice     2020-06-09
```

#### view

```zsh
redmine issues view $resource_id
```

result example

```
#              : $resource_id
Subject        : $subject
Status         : $status
Priority       : $priority
Assignee       : $assignee
Start date     : $start_date
Due date       : $due_date
%Done          : $parsent_done
Estimated time : $estimated_time

Description:
$description

Subtasks:
    $subtask

Related issues : $related_issue
```

#### create

```zsh
redmine issues create
```

#### update

```zsh
redmine issues update
```

#### delete

```zsh
redmine issues delete $resource_id
```

result example

```
delete #id: subject_name
```
### ticket

```zsh
redmine ticket
```

`redmine ticket`: aliased to `redmine issues`

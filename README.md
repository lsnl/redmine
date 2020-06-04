# redmine

## Usage

### projects

fetch projects list

```zsh
redmine projects list
```

result example

```
seminar
math-bof
workshop
```

### show

fetch project abstract

```
redmine show -p seminar
```

result example

```
Ticket Tracking
TBD    1
Done   0
Sum    1
Time Management:
Expected Man-hours    0:00
Working Hours         0:00
Member:
Alice, Bob, Carol, Dan
```

`redmine show` is equivalent `redmine show -p root`

### issues

issues

```zsh
redmine issues [list, view, create, update, delete]
```

You can see help by `redmine issues`.

#### list

```zsh
redmine issues list [-o] $header
```

result example

```
# Project         Status Priority Subject                  Assignee
1 研究:テーマ考案 ToDo   通常     2020-06-05 12:40-13:30   Alice
2 研究:テーマ考案 ToDo   通常     2020-06-07 12:40-13:30   Alice
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
redmine issues delete
```

### ticket

```zsh
redmine ticket
```

`redmine ticket`: aliased to `redmine issues`

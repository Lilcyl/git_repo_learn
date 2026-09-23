# Task Assistant

A simple Python command-line **Task Assistant** that allows users to create and manage a list of tasks.

The program provides a menu where users can:

1. Add a task
2. Display tasks
3. Mark a task as completed
4. View a task summary
5. Exit the application

## Features

### 1. Add Task

The user can enter a new task, which is added to the task list.

Example:

```text
Enter task: Complete Python exercise
Your task has been added successfully
```

Tasks are initially stored as **not completed**.

```python
{"Complete Python exercise": False}
```

---

### 2. Display Tasks

The program displays all tasks currently stored in the task list.

Example:

```text
1. {'Complete Python exercise': False}
2. {'Read Python notes': True}
```

If there are no tasks, the program displays:

```text
No tasks found.
```

---

### 3. Mark Task as Completed

The user can enter the name of a task they want to mark as completed.

For example:

```text
Enter task that you would like to mark as complete: Complete Python exercise
Task Complete Python exercise completed successfully
```

The task status changes from:

```python
{"Complete Python exercise": False}
```

to:

```python
{"Complete Python exercise": True}
```

If the task cannot be found, the program displays:

```text
Task not on the list
```

---

### 4. Task Summary

The program calculates and displays:

* Total number of tasks
* Number of completed tasks
* Number of pending tasks

Example:

```text
Total Task: 3
Completed Task: 1
Pending: 2
```

---

### 5. Exit

Selecting option `5` exits the application.

```text
Exiting...
```

## Functions

### `add_task()`

The `add_task()` function asks the user to enter a task and adds it to the task list.

Each new task is initially given a status of `False`, meaning it has not been completed.

```python
def add_task():
    taskname = input("Enter task: ")
    a = {taskname: False}
    tasklist.append(a)
```

### `view_tasks()`

The `view_tasks()` function checks whether the task list contains any tasks.

If the list is empty, it displays:

```text
No tasks found.
```

Otherwise, it loops through the task list and displays each task.

```python
def view_tasks():
    if len(tasklist) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasklist, start=1):
            print(f"{i}. {task}")
```

## Technologies Used

* **Python 3**
* Python lists
* Python dictionaries
* Functions
* `while` loops
* `for` loops
* `if / elif / else` statements
* Boolean values
* User input

## Requirements

You need:

* Python 3 installed on your computer
* A code editor such as VS Code

You can check whether Python is installed by running:

```bash
python --version
```

or:

```bash
python3 --version
```

## How to Run

1. Save the program as:

```text
task_assistant.py
```

2. Open a terminal in the folder containing the file.

3. Run the program:

```bash
python task_assistant.py
```

4. Enter your name when prompted.

5. Use the menu to manage your tasks.

## Example Session

```text
Enter your name: Alex
Hello Alex, what would you like to do?

To Add task, Press 1
To display task, Press 2
To mark task as completed, Press 3
To Show Task summary, Press 4
To exit App, Press 5
Enter your choice: 1

Enter task: Complete Python assignment
Your task has been added successfully

Enter your choice: 2

1. {'Complete Python assignment': False}

Enter your choice: 3

Enter task that you would like to mark as complete: Complete Python assignment
Task Complete Python assignment completed successfully

Enter your choice: 4

Total Task: 1
Completed Task: 1
Pending: 0

Enter your choice: 5

Exiting...
```

## Learning Objectives

This project demonstrates several beginner Python concepts:

* Creating and using variables
* Working with lists
* Working with dictionaries
* Creating and using functions
* Using `if`, `elif`, and `else`
* Using `for` and `while` loops
* Using Boolean values (`True` and `False`)
* Getting input from a user
* Building an interactive command-line application

## Future Improvements

Possible improvements to the application include:

* Delete a task
* Edit a task
* Display completed and pending tasks separately
* Give each task a unique ID
* Add task priorities such as High, Medium, and Low
* Add due dates
* Save tasks to a file
* Store tasks in an SQLite database
* Add error handling for invalid menu input
* Prevent duplicate task names

## Author

Created as a beginner Python command-line project to practise lists, dictionaries, functions, loops, conditions, and user input.

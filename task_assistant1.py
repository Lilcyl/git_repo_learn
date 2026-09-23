#Task Assistant
# 1. Add task
# 2. Display task
# 3. Mark tasks as completed
# 4. Task summary
# 5. Exit

user = input("Enter your name: ")
print(f"Hello {user}, what would you like to do?")

tasklist = []


# Function to add a task
def add_task():
    taskname = input("Enter task: ")
    a = {taskname: False}
    tasklist.append(a)
    print("Your task has been added successfully")


# Function to display all tasks
def view_tasks():
    if len(tasklist) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasklist, start=1):
            print(f"{i}. {task}")


menu = 0

while menu != 5:

    menu = int(input(
        "\nTo Add task, Press 1\n"
        "To display task, Press 2\n"
        "To mark task as completed, Press 3\n"
        "To Show Task summary, Press 4\n"
        "To exit App, Press 5\n"
        "Enter your choice: "
    ))

    # Add task
    if menu == 1:
        add_task()

    # Display tasks
    elif menu == 2:
        view_tasks()

    # Mark task as completed
    elif menu == 3:
        b = input("Enter task that you would like to mark as complete: ")

        if {b: False} in tasklist:
            i = tasklist.index({b: False})
            tasklist[i] = {b: True}
            print(f"Task {b} completed successfully")
        else:
            print("Task not on the list")

    # Task summary
    elif menu == 4:
        completed = 0
        total = len(tasklist)

        for b in tasklist:
            for c in b.values():
                if c:
                    completed = completed + 1

        pending = total - completed

        print(
            f"\nTotal Task: {total}\n"
            f"Completed Task: {completed}\n"
            f"Pending: {pending}"
        )

    # Exit
    elif menu == 5:
        print("Exiting...")

    # Invalid selection
    else:
        print("Wrong Selection, please try again")
